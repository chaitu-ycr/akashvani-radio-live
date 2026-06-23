cd %~dp0\..

uv sync --upgrade

uv run pyinstaller --onefile --noconsole --icon=.\src\akashvani_radio_live\app_icon.ico --name akashvani-radio-live .\src\akashvani_radio_live\app.py
