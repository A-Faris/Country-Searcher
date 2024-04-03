import requests
from rich.prompt import Prompt
from rich.console import Console
import argparse

from rich import print
from rich.traceback import install
install()

# Instead of using print(), you should use the Console from Rich instead.
console = Console(record=True)


def load_weather_for_location(lat: str, lng: str) -> dict:
    """Given a location, load the current weather for that location"""

    pass


def render_flights(flights: list) -> None:
    """Render a list of flights to the console using the Rich Library

    Consider using Panels, Grids, Tables or any of the more advanced
    features of the library"""

    console.print(flights)


def get_flights_from_iata(iata: str) -> list:
    """Given an IATA get the flights that are departing from that airport from Airlabs"""

    pass


def load_airport_JSON() -> list:
    """Load airport data from airports.json"""

    open(airports.json)
    pass


def find_airports_from_name(name: str, airport_data: list) -> list:
    """
    Find an airport from the airportData given a name
    Could return one or more airport objects
    """

    pass


def find_airport_from_iata(iata: str, airport_data: list) -> dict:
    """
    Find an airport from the airport_data given a name
    Should return exactly one airport object
    """

    pass


def get_airport() -> str:
    """Get the airport from the CLI"""
    parser = argparse.ArgumentParser(prog='airports',
                                     usage='%(prog)s [options]',
                                     description="name of the airport")

    parser.add_argument("--name",
                        type=str,
                        default="London Luton",
                        help="add airport name")
    args = parser.parse_args()

    name_upper = args.name.upper()

    return name_upper


if __name__ == "__main__":
    airport_data = load_airport_JSON()
    airport_search = get_airport()

# console.print_exception()
console.save_html("html_file.html")
