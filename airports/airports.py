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

FLIGHT_API_KEY = '3a4cdb65-8e74-44a2-bf9b-526d6f9f607b'
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
            "Temp": response.json()["current"]["temp_c"]}


def render_flights(flights: list) -> None:
    """Render a list of flights to the console using the Rich Library

    Consider using Panels, Grids, Tables or any of the more advanced features of the library"""
    table = Table(title="Flights")

    table.add_column("Flight No.", style="cyan", justify="right")
    table.add_column("Dept. Time", style="cyan", justify="right")
    table.add_column("Destination", style="purple")
    table.add_column("Delayed?", style="green", justify="right")
    table.add_column("Weather", style="green", justify="right")
    table.add_column("Temp", style="green", justify="right")

    for i in range(len(flights["Flight No."])):
        table.add_row(flights["Flight No."][i],
                      flights["Dept. Time"][i],
                      flights["Destination"][i],
                      flights["Delayed?"][i],
                      flights["Weather"][i],
                      str(flights["Temp"][i]))

    console.log(table)


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
    data = {"Flight No.": [],
            "Dept. Time": [],
            "Destination": [],
            "Delayed?": [],
            "Weather": [],
            "Temp": []}

    for airport in track(airport_data, description="Working..."):
        if airport["dep_iata"] == iata:
            data["Flight No."].append(airport["flight_number"])
            data["Dept. Time"].append(airport["dep_time_utc"])
            for name in load_airport_JSON():
                if name["iata"] == airport["arr_iata"]:
                    condition = load_weather_for_location(
                        name['lat'], name['lon'])
                    data["Weather"].append(condition["Weather"])
                    data["Temp"].append(condition["Temp"])
                    if name["name"]:
                        data["Destination"].append(name["name"])
                    else:
                        data["Destination"].append(None)
                    break
            if airport["dep_delayed"]:
                data["Delayed?"].append(f"{airport["dep_delayed"]} mins")
            else:
                data["Delayed?"].append("On Time")

    return data


def get_airport() -> str:
    """Get the airport from the CLI"""
    parser = argparse.ArgumentParser(prog='airports',
                                     usage='%(prog)s [options]',
                                     description="name of the airport")

    parser.add_argument("--name",
                        type=str,
                        default="London Gatwick Airport",
                        help="add file format")

    parser.add_argument("--export",
                        type=str,
                        default="json",
                        help="add airport name")

    args = parser.parse_args()

    name = args.name.title()

    print(name)
    if name == "html":
        console.save_html(f"html_file_{datetime.now()}.html")
    elif name == "json":
        save_as_json(data)

    return name


if __name__ == "__main__":
    console.log(
        "✈️✈️✈️✈️✈️✈️✈️✈️\nWelcome to the Airports Informer Tool\n✈️✈️✈️✈️✈️✈️✈️✈️")

    airport_data = load_airport_JSON()
    airport_search = get_airport()
    airport_names = find_airports_from_name(airport_search, airport_data)

    if len(airport_names) > 1:
        airport = Prompt.ask(
            "Multiple airports found, please choose one: ", choices=airport_names)
    airport = airport_names[0]

    for data in airport_data:
        if airport == str(data["name"]):
            iata = data["iata"]
            break

    flights = get_flights_from_iata(iata)

    airport_landing = find_airport_from_iata(iata, flights)

    render_flights(airport_landing)
