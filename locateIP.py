import requests

import json

import re

def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)

    return text

def jload(obj):

    loaded_json = json.loads(formatted_json)

    return loaded_json


def get_ip_location_json(parameter):

    response = requests.get("http://ip-api.com/json/"+parameter)

    if (response.status_code == 200):

        return response.json()

    else :

        print ("Unsuccessful Request with error code :",response.status_code)

        return None

# Validate user input whether is an IP address or a domain name
def validate_address(ip_address):

    ip_valid = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip_address)

    domain_valid = re.match(r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*",ip_address)

    if (ip_valid != None or domain_valid != None):

        return True

    else:

        return False

while True:

    ip_address = input ("Please enter an IP Address or a domain name: ")

    validation = validate_address(ip_address)

    if (validation == True):

        break

ip_location_json = get_ip_location_json(ip_address)

formatted_json = jprint(ip_location_json)

loaded_json = jload(ip_location_json)

print ("Country:",loaded_json['country'],"[",loaded_json['countryCode'],"]")

print ("City:",loaded_json['city'])

print ("Region:",loaded_json['region'])
