from pprint import PrettyPrinter

import requests

pp = PrettyPrinter(indent=4)


# the api endpoint where the challenge data comes from.
# i found this by just inspecting the "network" tab of the challenges page
# (https://www.strava.com/challenges) to see if any of the resources were
# json
CHALLENGES_ENDPOINT = "https://www.strava.com/frontend/challenges"


def query_api() -> dict:
    """
    Makes a request to the Strava endpoint which yields a json object
    containing the challenge data
    """
    response = requests.get(CHALLENGES_ENDPOINT)
    response.raise_for_status()
    return response.json()


def get_unique_challenges(json: dict) -> list[dict]:
    """
    Given `json`, i.e. the return value of `query_api`, this function gets
    all the challenges, puts them into a list, removes any duplicates, and
    returns them
    """
    # At the top of the json object there's a key called "gallerySections"
    # under which there are keys like "recommended", "run", "ride", etcetera.
    # Each of those has a "challenges" key, which is a list of dicts
    challenges = []
    for section in json["gallerySections"].values():
        for challenge in section["challenges"]:
            if challenge in challenges:
                continue
            challenges.append(challenge)
    return challenges


def main():

    json = query_api()

    challenges = get_unique_challenges(json)

    pp.pprint(challenges)


if __name__ == "__main__":
    main()
