from pathlib import Path
import os


def AddFile(month, year, json):
    path = Path.cwd() / "articles"

    path = path / str(year)
    if not os.path.exists(path):
        path.mkdir()

    if path is not None:
        try:
            path = path / f"{getMonth(month)}_articles.json"
            with open(path, "w") as file:
                file.write(json)
            return path
        except Exception as e:
            print(e)
            raise Exception(e)


def getMonth(mon):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    return months[mon - 1]
