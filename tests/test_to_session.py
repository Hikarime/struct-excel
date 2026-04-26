from struct_excel.transform import to_session


def test_to_session():
    from tests.test_data import RAW, EXPECTED_COURSES, EXPECTED_SESSIONS

    sessions = to_session(RAW, EXPECTED_COURSES)

    assert len(sessions) == len(EXPECTED_SESSIONS)

    for i, session in enumerate(sessions):
        assert session.session_id == EXPECTED_SESSIONS[i].session_id
        assert session.course_id == EXPECTED_SESSIONS[i].course_id
        assert session.start_datetime == EXPECTED_SESSIONS[i].start_datetime
        assert session.end_datetime == EXPECTED_SESSIONS[i].end_datetime
        assert session.mode == EXPECTED_SESSIONS[i].mode
        assert session.duration == EXPECTED_SESSIONS[i].duration


def test_to_session_empty():
    sessions = to_session([], [])
    assert sessions == []


def test_to_session_deduplication():
    from datetime import datetime
    from struct_excel.models import Course, RawRow

    raw_dup = [
        RawRow(
            reg_date=datetime(2026, 1, 15),
            student_full_name="Student 1",
            student_email="student1@example.com",
            student_company="Company",
            student_job_title="Title",
            country="USA",
            exception="None",
            phone="123-456-7890",
            course="Feb 10 2026 | [Online] Python Basics [2hr]",
            gender="Male",
            sector="Private",
            supervisor_name="Supervisor",
            supervisor_email="supervisor@example.com",
            it_background="Yes",
            experience="2-5 years",
            completed="Yes",
            payment_status="Paid",
        ),
        RawRow(
            reg_date=datetime(2026, 1, 16),
            student_full_name="Student 2",
            student_email="student2@example.com",
            student_company="Company",
            student_job_title="Title",
            country="USA",
            exception="None",
            phone="098-765-4321",
            course="Feb 10 2026 | [Online] Python Basics [2hr]",
            gender="Female",
            sector="Private",
            supervisor_name="Supervisor",
            supervisor_email="supervisor@example.com",
            it_background="No",
            experience="0-2 years",
            completed="No",
            payment_status="Pending",
        ),
    ]
    courses = [
        Course(course_id=1, course_name="Python Basics"),
    ]
    sessions = to_session(raw_dup, courses)
    assert len(sessions) == 1
    assert sessions[0].session_id == 1
