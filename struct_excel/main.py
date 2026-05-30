from struct_excel.excel import get_excel_sheet, sheet_to_db
import logging
import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Process Excel workbook into normalized outputs."
    )
    parser.add_argument(
        "--src",
        required=True,
        help="Path to source Excel file",
    )
    parser.add_argument(
        "--name",
        required=True,
        help="Name of the sheet to be normalized",
    )
    parser.add_argument(
        "--course",
        required=True,
        help="Path to training list Excel file",
    )

    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    DB_PATH = "sqlite:///./dist/test.db"
    ERR_XLSX = "./dist/err.xlsx"

    args = parse_args()
    excel_path = args.src
    sheet_name = args.name
    course_list_path = args.course

    dist_dir = Path("dist")
    dist_dir.mkdir(parents=True, exist_ok=True)

    ws = get_excel_sheet(excel_path, sheet_name)
    course_list_ws = get_excel_sheet(course_list_path, "Sheet1")

    sheet_to_db(ws, DB_PATH, ERR_XLSX, course_list_ws)


if __name__ == "__main__":
    main()
