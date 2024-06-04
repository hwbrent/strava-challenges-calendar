from pprint import PrettyPrinter

import requests

pp = PrettyPrinter(indent=4)


def main():
    response = requests.get("https://www.strava.com/frontend/challenges")
    response.raise_for_status()

    json = response.json()
    # pp.pprint(json)

    challenges = set(
        challenge
        for section in json["gallerySections"].values()
        for challenge in section["challenges"]
    )

    pp.pprint(challenges)


if __name__ == "__main__":
    main()
