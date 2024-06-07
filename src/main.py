from pprint import PrettyPrinter

import requests

# This url yields an HTML paeg containing the challenges. The `type`
# parameter determines whether we get past, present or future challenges.
# I found these urls by looking at the "Network" tab of the FireFox devtools
BASE_URL = "https://www.kom.club/sections/challenges_amz.asp?filter=all&type="
types = (
    "complete",  # "Passed"
    "active",  # "Active"
    "upcoming",  # "Up Coming"
)


def get_html(_type=types[1]) -> str:
    """
    Given the desired type of challenges, this function returns the HTML of
    the page on kom.club
    """

    url = BASE_URL + _type

    response = requests.get(url)
    response.raise_for_status()

    html = response.text

    return html


def main():
    html = get_html()


if __name__ == "__main__":
    main()
