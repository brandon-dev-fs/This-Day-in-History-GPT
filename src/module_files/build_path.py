import os
from pathlib import Path

from modules_dates.get_month_name import get_month_name

def build_path(type, date):
    print("Building path... ")
    path = Path.cwd() / "src" / "outputs" / type

    # Checks if type path exists. If not makes the directory for the type
    if not os.path.exists(path):
        path.mkdir()

    path = path / str(date.year) 
    # Checks if year path exists in type. If not makes the directory for that year
    if not os.path.exists(path):
        path.mkdir()

    # returns a path with the file int the file to be read and/or written in its file path
    filename = f"{get_month_name(int(date.month))}_{type}.json"

    return path / filename