from openpyxl.worksheet.worksheet import Worksheet

from models import RawRow


def read_raw_row(ws: Worksheet) -> list[RawRow]:
    headers = {cell.value: idx for idx, cell in enumerate(ws[1])}
    rows = []

    for row in ws.iter_rows(min_row=2, values_only=True):
        student_job_title = _conv_str_none(row[headers["Job Title"]])
        exception = _conv_str_none(row[headers["Exception"]])
        supervisor_name = _conv_str_none(row[headers["Supervisor's Name"]])
        supervisor_email = _conv_str_none(row[headers["Supervisor's Email"]])
        completed = _conv_str_none(row[headers["Completed"]])
        payment_status = _conv_str_none(row[headers["Payment Status"]])
        experience = _conv_str_none(row[headers["IT/Cybersecurity work exp (yrs)"]])
        it_background = _conv_str_none(row[headers["IT/Cybersecurity bckgrd (Yes/No)"]])

        rows.append(
            RawRow(
                reg_date=row[headers["Reg Date"]],
                student_full_name=str(row[headers["Full Name"]]),
                student_email=str(row[headers["Email"]]),
                student_company=str(row[headers["Company"]]),
                student_job_title=student_job_title,
                country=str(row[headers["Country"]]),
                exception=exception,
                phone=str(row[headers["Phone"]]),
                course=str(row[headers["Course"]]),
                gender=str(row[headers["Gender"]]),
                sector=str(row[headers["Sector"]]),
                supervisor_name=supervisor_name,
                supervisor_email=supervisor_email,
                it_background=it_background,
                experience=experience,
                completed=completed,
                payment_status=payment_status,
            )
        )

    return rows


def _conv_str_none(value) -> str | None:
    if value is None or value == "":
        return None
    return value
