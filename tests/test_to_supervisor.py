from struct_excel.transform import to_supervisor


def test_to_supervisor():
    from tests.test_data import RAW, EXPECTED_SUPERVISORS

    supervisors = to_supervisor(RAW)

    assert len(supervisors) == len(EXPECTED_SUPERVISORS)

    for i, sup in enumerate(supervisors):
        assert sup.supervisor_id == EXPECTED_SUPERVISORS[i].supervisor_id
        assert sup.full_name == EXPECTED_SUPERVISORS[i].full_name
        assert sup.email == EXPECTED_SUPERVISORS[i].email


def test_to_supervisor_empty():
    supervisors = to_supervisor([])
    assert supervisors == []


def test_to_supervisor_deduplication():
    from datetime import datetime
    from struct_excel.models import RawRow

    raw_same_sup = [
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
            supervisor_name="Jane Smith",
            supervisor_email="jane.smith@example.com",
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
            supervisor_name="Jane Smith",
            supervisor_email="jane.smith@example.com",
            it_background="No",
            experience="0-2 years",
            completed="No",
            payment_status="Pending",
        ),
    ]
    supervisors = to_supervisor(raw_same_sup)
    assert len(supervisors) == 1
    assert supervisors[0].full_name == "Jane Smith"
    assert supervisors[0].supervisor_id == 1


def test_to_supervisor_empty_string():
    from datetime import datetime
    from struct_excel.models import RawRow

    raw = [
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
            sector="Student",
            supervisor_name="",
            supervisor_email="",
            it_background="Yes",
            experience="<1 year",
            completed="Yes",
            payment_status="Paid",
        ),
    ]
    supervisors = to_supervisor(raw)
    assert len(supervisors) == 0
