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
        "--name", required=True, help="Name of the sheet to be normalized"
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

    dist_dir = Path("dist")
    dist_dir.mkdir(parents=True, exist_ok=True)

    ws = get_excel_sheet(excel_path, sheet_name)
    sheet_to_db(ws, DB_PATH, ERR_XLSX)


if __name__ == "__main__":
    main()
