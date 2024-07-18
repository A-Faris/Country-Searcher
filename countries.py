from requests import get
from rich.traceback import install

install()


class APIError(Exception):
    """Describes an error triggered by a failing API call."""

    def __init__(self, message: str, code: int = 500):
        """Creates a new APIError instance."""
        self.message = message
        self.code = code


def fetch_data(country_name: str) -> dict:
    """Returns a dict of country data from the API."""
    response = get(
        f'https://restcountries.com/v3.1/name/{country_name.lower()}', timeout=10)

    if response.status_code == 404:
        raise APIError("Unable to locate matching country.", 404)
    if response.status_code == 500:
        raise APIError("Unable to connect to server.")

    if type(response.json()) == list:
        data = response.json()[0]
    else:
        data = response.json()
    return {"name": data.get("name"),
            "flag": data.get("flag"),
            "languages": data.get("languages")}


def main():
    """Repeatedly prompts the user for country names and displays the result."""
    print("\n####################")
    print("Welcome to the REST Countries Searcher")
    print("####################\n")

    while True:
        entry = input("Search for a country: ")
        print(f"You searched for: {entry}")
        print("Fetching...\n")
        try:
            country_data = fetch_data(entry)
            print(country_data)
        except APIError as e:
            print(e.message)
        print(" ")


if __name__ == "__main__":
    main()
