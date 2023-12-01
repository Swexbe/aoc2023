import requests as requests

cookie = "53616c7465645f5fb20254bdf8e4103871772c4579c2fe23f9deea33d69788b9d9aac1d3676ddaeae35fb0ac4243222003015602b3a5d7af718dca2c7c7be80d"


def get_input(day: int, year: int = 2023) -> str:
    res = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={"session": cookie})
    return res.text.strip()
