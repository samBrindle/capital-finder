from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    url_components = parse.urlsplit(self.path)
    query_string_list = parse.parse_qsl(url_components.query)
    query_dict = dict(query_string_list)

    if "capital" in query_dict:
        url = "https://restcountries.com/v3.1/capital/"
        response = requests.get(url + query_dict["capital"])
        data = response.json()
        countries = []
        for country_data in data:
            country = country_data["name"]["common"]
            countries.append(country)

        message = f"{query_dict['capital']} is the capital of {countries[0]}"
    elif "name" in query_dict:
        url = "https://restcountries.com/v2/name/"
        response = requests.get(url + query_dict["name"])
        data = response.json()
        countries = []
        for country_data in data:
            country = country_data["capital"]
            countries.append(country)

        message = f"The capital of {query_dict['name']} is {countries[0]}"
    else:
        message = "Give me a capital or a country"

    self.wfile.write(message.encode())
    return
