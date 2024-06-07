from pprint import PrettyPrinter

import requests

# These urls yield HTML pages containing the challenges. There is a `type`
# parameter which determines whether we get the past, present or future
# challenges.
# I found these urls by looking at the "Network" tab of the FireFox devtools
BASE_URL = "https://www.kom.club/sections/challenges_amz.asp?filter=all&type="
PASSED_URL = BASE_URL + "complete"
ACTIVE_URL = BASE_URL + "active"
UPCOMING_URL = BASE_URL + "upcoming"


def main():
    pass


if __name__ == "__main__":
    main()
