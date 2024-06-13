from pprint import PrettyPrinter

import requests
from bs4 import BeautifulSoup

# This url yields an HTML paeg containing the challenges. The `type`
# parameter determines whether we get past, present or future challenges.
# I found these urls by looking at the "Network" tab of the FireFox devtools
BASE_URL = "https://www.kom.club/sections/challenges_amz.asp?filter=all&type="
types = (
    "complete",  # "Passed"
    "active",  # "Active"
    "upcoming",  # "Up Coming"
)


def get_kom_club_html(_type=types[1]) -> str:
    """
    Given the desired type of challenges, this function returns the HTML of
    the page on kom.club
    """

    url = BASE_URL + _type

    response = requests.get(url)
    response.raise_for_status()

    html = response.text

    return html


def get_strava_challenge_urls(kom_club_html: str) -> set[str]:
    """
    Given the HTML for the kom.club page containing all the challenges, this
    function gets the Strava URL for each of the challenges, and returns them
    as a set of strings
    """

    # Specify that we're parsing HTML, rather than XML or w/e
    soup = BeautifulSoup(kom_club_html, features="html.parser")

    # From manual inspection, there are a bunch of <a>s whose href attribute
    # is the url that we want. The url always starts with
    # 'http://www.strava.com/challenges/'. So we can use CSS selectors to
    # find these tags based off that attribute

    a_tags = soup.select("a[href^='http://www.strava.com/challenges/']")

    # We use a 'set' because otherwise there are two of each URL
    hrefs = set([tag["href"] for tag in a_tags])

    return hrefs


def main():
    html = get_kom_club_html()
    challenge_urls = get_strava_challenge_urls(html)
    print(challenge_urls)


if __name__ == "__main__":
    main()
