from operator import ge
import requests
from rich.prompt import Prompt
from rich.console import Console
import argparse

import json
from rich import print
from rich.table import Table
from rich.progress import track
from datetime import datetime
from rich.traceback import install
install()

console = Console(record=True)

FLIGHT_API_KEY = '4011fa89-ed51-416d-8932-0585e4889e2e'
WEATHER_API_KEY = '377d489eceb84769ad5103828240404'


def save_as_json(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    f.close()


def load_weather_for_location(lat: str, lng: str) -> dict:
    """Given a location, load the current weather for that location"""

    response = requests.get(
        f"http://api.weatherapi.com/v1/current.json?q={lat},{lng}&key={WEATHER_API_KEY}")

    response.raise_for_status()

    return {"Weather": response.json()["current"]["condition"]["text"],
            "Temp": str(response.json()["current"]["temp_c"])}


def render_flights(flights: list[dict], airport_data: list[dict]) -> Table:
    """
    Render a list of flights to the console using the Rich Library
    Consider using Panels, Grids, Tables or any of the more advanced features of the library
    """

    table = Table(title="Flights")

    table.add_column("Flight No.", style="cyan", justify="right")
    table.add_column("Dept. Time", style="cyan", justify="right")
    table.add_column("Destination", style="purple")
    table.add_column("Delayed?", style="green", justify="right")
    table.add_column("Weather", style="green", justify="right")
    table.add_column("Temp", style="green", justify="right")

    # print([value[0] for value in flights.values()])
    for flight in track(flights):

        flight["airline_name"] = " "
        flight["weather"] = " "
        flight["temp"] = " "

        for airport in airport_data:
            if airport["iata"] == flight["arr_iata"]:
                flight["airline_name"] = airport["name"]
                condition = load_weather_for_location(
                    airport["lat"], airport["lon"])
                flight["weather"] = condition["Weather"]
                flight["temp"] = condition["Temp"]
                break

        if flight["delayed"]:
            flight["delayed"] = f"{flight["delayed"]} mins"
        else:
            flight["delayed"] = "On Time"

        table.add_row(flight["flight_number"],
                      flight["dep_time"],
                      flight["airline_name"],
                      flight["delayed"],
                      flight["weather"],
                      flight["temp"])

    return table


def get_flights_from_iata(iata: str) -> list:
    """Given an IATA get the flights that are departing from that airport from Airlabs"""

    response = requests.get(
        f"https://airlabs.co/api/v9/schedules?dep_iata={iata}&api_key={FLIGHT_API_KEY}")

    response.raise_for_status()

    return response.json()["response"]


def load_airport_JSON() -> list:
    """Load airport data from airports.json"""

    f = open('airports.json')
    data = json.load(f)
    f.close()
    return data


def find_airports_from_name(name: str, airport_data: list) -> list[dict]:
    """
    Find an airport from the airportData given a name
    Could return one or more airport objects
    """
    return [airport for airport in airport_data if name in str(airport.get("name"))]


def find_iata_from_airport(name: str, airport_data: list):
    """
    Find an iata from the airport_data given an airport name
    Should return exactly one airport object
    """
    for airport in airport_data:
        if name == airport["name"]:
            return airport["iata"]


def get_airport() -> str:
    """Ask user for airport name"""
    return input("Type name of airport: ").title()


def load_argument() -> dict:
    """Get the airport from the CLI"""
    parser = argparse.ArgumentParser(prog='airports',
                                     usage='%(prog)s [options]',
                                     description="add name of the airport and file format")

    parser.add_argument("--name",
                        type=str,
                        default="London",
                        help="add name of airport")

    parser.add_argument("--export",
                        type=str,
                        default="json",
                        help="add file format (json/html)")

    args = parser.parse_args()

    export = args.export.lower()
    name = args.name.title()

    return {"name": name,
            "export": export}


if __name__ == "__main__":
    console.log(
        "✈️✈️✈️✈️✈️✈️✈️✈️\nWelcome to the Airports Informer Tool\n✈️✈️✈️✈️✈️✈️✈️✈️")

    airport_data = load_airport_JSON()

    args = load_argument()
    name = args["name"]
    export = args["export"]
    print(f"Airport name is {name} and export file format is {export}")

    if not name:
        name = get_airport()

    while True:
        airport_names = find_airports_from_name(name, airport_data)

        if airport_names:
            break

        print("\nAirport name is not in the database. Try again")
        name = get_airport()

    if len(airport_names) > 1:
        name = Prompt.ask(
            "Multiple airports found, please choose one: ", choices=[airport.get("name") for airport in airport_names], default=airport_names[0].get("name"))

    for airport in airport_names:
        if name == airport["name"]:
            iata = airport["iata"]

    flights = get_flights_from_iata(iata)

    table = render_flights(flights, airport_data)

    console.log(table)

    if args["export"] == "html":
        console.save_html(f"html_file_{datetime.now()}.html")
    elif args["export"] == "json":
        save_as_json(flights)
