import logging
import sys

from openpyxl.worksheet.worksheet import Worksheet
from struct_excel.database import init_db, model_to_db
from struct_excel.models import Course, CourseSession, Enrollment, Student, Supervisor
from struct_excel.normalization import normalize_sheet
from openpyxl import Workbook, load_workbook
from struct_excel.reader import read_raw_row
from struct_excel.transform import (
    to_course,
    to_enrollment,
    to_session,
    to_student,
    to_supervisor,
)

logger = logging.getLogger(__name__)


def normalize_excel_sheet(
    sheet: Worksheet, err_path: str
) -> tuple[
    list[Supervisor], list[Course], list[Student], list[CourseSession], list[Enrollment]
]:
    err_wb = Workbook()
    err_ws = err_wb.create_sheet(sheet.title)
    normalize_sheet(sheet, err_ws)
    err_wb.save(err_path)

    try:
        raw_rows = read_raw_row(sheet)
    except ValueError as e:
        logger.error(str(e))
        raise

    supervisors = to_supervisor(raw_rows)
    courses = to_course(raw_rows)
    students = to_student(raw_rows, supervisors)
    sessions = to_session(raw_rows, courses)
    enrollments = to_enrollment(raw_rows, students, courses, sessions)

    return (supervisors, courses, students, sessions, enrollments)


def sheet_to_db(sheet: Worksheet, db_path: str, err_path: str):
    # Create error workbook and worksheet.
    err_wb = Workbook()
    err_wb.remove(err_wb.active)  # pyright:ignore
    err_ws = err_wb.create_sheet(sheet.title)

    # Normalize the sheet. And get entities.
    normalize_sheet(sheet, err_ws)
    supervisors, courses, students, sessions, enrollments = normalize_excel_sheet(
        sheet, err_path
    )

    # Create database.
    engine = init_db(db_path)

    # Store entities into the database.
    model_to_db(engine, supervisors)
    model_to_db(engine, courses)
    model_to_db(engine, students)
    model_to_db(engine, sessions)
    model_to_db(engine, enrollments)


def get_excel_sheet(path: str, name: str) -> Worksheet:
    wb = load_workbook(path)

    try:
        return wb[name]
    except KeyError:
        logger.error(f"invalid sheet name, available sheets: {wb.sheetnames}")
        sys.exit(1)
