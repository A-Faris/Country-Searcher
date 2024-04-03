import requests
from rich.prompt import Prompt
from rich.console import Console
import argparse

import json
from rich import print
from rich.traceback import install
install()

# Instead of using print(), you should use the Console from Rich instead.
console = Console(record=True)

API_KEY = '3a4cdb65-8e74-44a2-bf9b-526d6f9f607b'


def load_weather_for_location(lat: str, lng: str) -> dict:
    """Given a location, load the current weather for that location"""

    pass


def render_flights(flights: list) -> None:
    """Render a list of flights to the console using the Rich Library

    Consider using Panels, Grids, Tables or any of the more advanced features of the library"""
    print(flights)
    print(type(flights))
    print(len(flights))


def get_flights_from_iata(iata: str) -> list:
    """Given an IATA get the flights that are departing from that airport from Airlabs"""

    response = requests.get(
        f"https://airlabs.co/api/v9/schedules?dep_iata={iata}&api_key={API_KEY}")

    response.raise_for_status()
    return response.json()["response"]


def load_airport_JSON() -> list:
    """Load airport data from airports.json"""

    f = open('airports.json')
    data = json.load(f)
    f.close()
    return data


def find_airports_from_name(name: str, airport_data: list) -> list:
    """
    Find an airport from the airportData given a name
    Could return one or more airport objects
    """
    airports = []
    for airport in airport_data:
        if name in str(airport["name"]):
            airports.append(airport["name"])
    return airports

    # return [airport.get("name") for airport in airport_data if name in str(airport.get("name"))]


def find_airport_from_iata(iata: str, airport_data: list) -> dict:
    """
    Find an airport from the airport_data given a name
    Should return exactly one airport object
    """
    foo = {"departing iata": iata,
           "arriving iata": []}
    for airport in airport_data:
        if airport["dep_iata"] == iata:
            foo["arriving iata"].append(airport["arr_iata"])
    return foo


def get_airport() -> str:
    """Get the airport from the CLI"""
    parser = argparse.ArgumentParser(prog='airports',
                                     usage='%(prog)s [options]',
                                     description="name of the airport")

    parser.add_argument("--name",
                        type=str,
                        default="London Heathrow Airport",
                        help="add airport name")

    args = parser.parse_args()

    name = args.name.title()

    return name


if __name__ == "__main__":
    airport_data = load_airport_JSON()
    airport_search = get_airport()
    airport_names = find_airports_from_name(airport_search, airport_data)
    airport = airport_names[0]
    if len(airport_names) > 1:
        airport = Prompt.ask(
            "Multiple airports found, please choose one: ", choices=airport_names)

    for data in airport_data:
        if airport == str(data["name"]):
            iata = data["iata"]
            break

    flights = get_flights_from_iata(iata)

    airport_landing = find_airport_from_iata(iata, flights)

    render_flights(airport_landing)


# console.print_exception()
console.save_html("html_file.html")
