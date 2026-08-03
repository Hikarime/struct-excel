import os
import sys
from pathlib import Path


def main():
    import streamlit.web.bootstrap as bootstrap
    from streamlit import config as _config

    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
    main_script_path = str(base / "struct_excel" / "app.py")

    _config._main_script_path = os.path.abspath(main_script_path)
    bootstrap.load_config_options(flag_options={"global.developmentMode": False})

    sys.argv = [main_script_path]
    bootstrap.run(main_script_path, False, [], {})


if __name__ == "__main__":
    main()
