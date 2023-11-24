import requests as requests

cookie = ""


def get_input(day: int, year: int = 2023) -> str:
    res = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={"session": cookie})
    return res.text.strip()
