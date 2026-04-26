from struct_excel.transform import to_course


def test_to_course():
    from tests.test_data import RAW, EXPECTED_COURSES

    courses = to_course(RAW)

    assert len(courses) == len(EXPECTED_COURSES)

    for i, course in enumerate(courses):
        assert course.course_id == EXPECTED_COURSES[i].course_id
        assert course.course_name == EXPECTED_COURSES[i].course_name


def test_to_course_empty():
    courses = to_course([])
    assert courses == []


def test_to_course_deduplication():
    from datetime import datetime
    from struct_excel.models import RawRow

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
    courses = to_course(raw_dup)
    assert len(courses) == 1
    assert courses[0].course_name == "Python Basics"
    assert courses[0].course_id == 1
