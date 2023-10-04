#! /usr/bin/env python3
import sys
import requests
import json
import socket
import requests
import subprocess, shlex


def main():
    # base API string for weather.gov
    weather_s = "https://api.weather.gov/points/"

    
    # sys.argv[1] gives us the command line input
    # sys.argv[0] is the name of the python file
    print(weather_s+sys.argv[1])

    # use the commandline input and the weather_s to make API call
    response = requests.get(weather_s+sys.argv[1])

    # convert it to json
    js = json.loads(response.text)

    # find the forecast URL based on the API page
    forecast_URL = js['properties']['forecast']

    #print link that we use for next API call
    print(forecast_URL)

    # call the API again to get theforecast
    final_response = requests.get(forecast_URL)

    #parse json
    js = json.loads(final_response.text)

    #print the forecast
    print(js['properties']['periods'][0]['detailedForecast'])
    
    ip = socket.gethostbyname("www.google.com")
    print(ip)
    loc = str(subprocess.check_output(["whois",ip]))
    li = list(loc.split("\\n"))
    addr = ""
    for i in li:
        if i.startswith("Address:"or"City:"or"StateProv:"or
        "PostalCode:"or"Country:"):
            breakpoint()
            addr=addr+i
            
    print(addr)
    
    


    

if __name__ == "__main__":
    main()

