This repository stores script for structuring Excel data file provided by MCMC and BlackBerry Cybersecurity Centre of Excellence (CCOE).

## Installation

### From Release

Access [GitHub Release](https://github.com/FovirDev/struct-excel/releases/latest) and download the binary matches your OS.

| OS      | Binary                                                                                                                   |
| ------- | ------------------------------------------------------------------------------------------------------------------------ |
| Windows | [`struct-excel-windows.exe`](https://github.com/FovirDev/struct-excel/releases/latest/download/struct-excel-windows.exe) |
| Linux   | [`struct-excel-linux`](https://github.com/FovirDev/struct-excel/releases/latest/download/struct-excel-linux)             |
| macOS   | [`struct-excel-macos`](https://github.com/FovirDev/struct-excel/releases/latest/download/struct-excel-macos)             |

### From Source

1. Clone the repository

   ```bash
   git clone https://github.com/FovirDev/struct-excel.git
   cd struct-excel
   ```

2. Create and activate virtual environment (Python >= `3.13`)

   ```bash
   python -m venv .venv

   # Linux
   source .venv/bin/activate

   # Windows
   .venv/bin/Activate.ps1
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Execute the program

   ```bash
   streamlit run struct_excel/app.py
   ```

## Usage

See [docs/usage.md](docs/usage.md)

## Documentation

All documentations are available under the [`docs/`](docs/) folder.

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md)
