from struct_excel.transform import to_student


def test_to_student():
    from tests.test_data import RAW, EXPECTED_STUDENTS, EXPECTED_SUPERVISORS

    students = to_student(RAW, EXPECTED_SUPERVISORS)

    assert len(students) == len(EXPECTED_STUDENTS)

    for i, student in enumerate(students):
        assert student.student_id == EXPECTED_STUDENTS[i].student_id
        assert student.full_name == EXPECTED_STUDENTS[i].full_name
        assert student.email == EXPECTED_STUDENTS[i].email
        assert student.gender == EXPECTED_STUDENTS[i].gender
        assert student.it_background == EXPECTED_STUDENTS[i].it_background
        assert student.experience_min_years == EXPECTED_STUDENTS[i].experience_min_years
        assert student.experience_max_years == EXPECTED_STUDENTS[i].experience_max_years
        assert student.sector == EXPECTED_STUDENTS[i].sector
        assert student.supervisor_id == EXPECTED_STUDENTS[i].supervisor_id


def test_to_student_empty():
    students = to_student([], [])
    assert students == []


def test_to_student_gender_parsing():
    from datetime import datetime
    from struct_excel.models import Gender, RawRow, Supervisor

    raw_gender = [
        RawRow(
            reg_date=datetime(2026, 1, 15),
            student_full_name="John Doe",
            student_email="john@example.com",
            student_company="Company",
            student_job_title="Title",
            country="USA",
            exception="None",
            phone="123-456-7890",
            course="Feb 10 2026 | [Online] Python Basics [2hr]",
            gender="male",
            sector="Private",
            supervisor_name="Supervisor",
            supervisor_email="supervisor@example.com",
            it_background="Yes",
            experience="2-5 years",
            completed="Yes",
            payment_status="Paid",
        ),
    ]
    supervisors = [
        Supervisor(
            supervisor_id=1, full_name="Supervisor", email="supervisor@example.com"
        )
    ]
    students = to_student(raw_gender, supervisors)
    assert len(students) == 1
    assert students[0].gender == Gender.MALE


def test_to_student_it_background_parsing():
    from datetime import datetime
    from struct_excel.models import RawRow, Supervisor

    raw_it = [
        RawRow(
            reg_date=datetime(2026, 1, 15),
            student_full_name="John Doe",
            student_email="john@example.com",
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
            it_background="yes",
            experience="2-5 years",
            completed="Yes",
            payment_status="Paid",
        ),
    ]
    supervisors = [
        Supervisor(
            supervisor_id=1, full_name="Supervisor", email="supervisor@example.com"
        )
    ]
    students = to_student(raw_it, supervisors)
    assert len(students) == 1
    assert students[0].it_background is True


def test_to_student_experience_parsing():
    from datetime import datetime
    from struct_excel.models import RawRow, Supervisor

    raw_exp = [
        RawRow(
            reg_date=datetime(2026, 1, 15),
            student_full_name="John Doe",
            student_email="john@example.com",
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
            experience=">5 years",
            completed="Yes",
            payment_status="Paid",
        ),
    ]
    supervisors = [
        Supervisor(
            supervisor_id=1, full_name="Supervisor", email="supervisor@example.com"
        )
    ]
    students = to_student(raw_exp, supervisors)
    assert len(students) == 1
    assert students[0].experience_min_years == 5
    assert students[0].experience_max_years == 100


def test_to_student_experience_nil():
    from datetime import datetime
    from struct_excel.models import RawRow, Supervisor

    raw_exp = [
        RawRow(
            reg_date=datetime(2026, 1, 15),
            student_full_name="John Doe",
            student_email="john@example.com",
            student_company="Company",
            student_job_title="Title",
            country="USA",
            exception="None",
            phone="123-456-7890",
            course="Feb 10 2026 | [Online] Python Basics [2hr]",
            gender="Male",
            sector="Government",
            supervisor_name="Supervisor",
            supervisor_email="supervisor@example.com",
            it_background="No",
            experience="Nil",
            completed="Yes",
            payment_status="Paid",
        ),
    ]
    supervisors = [
        Supervisor(
            supervisor_id=1, full_name="Supervisor", email="supervisor@example.com"
        )
    ]
    students = to_student(raw_exp, supervisors)
    assert len(students) == 1
    assert students[0].experience_min_years == 0
    assert students[0].experience_max_years == 0
