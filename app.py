import os
import random
import socket
import time

import requests

greetings = [
    "Hello",
    "Hi",
    "Howdy",
    "Hey there",
    "Good day",
    "Yo",
    "Aloha",
    "Ciao",
    "Hola",
    "Hallo",
    "Oi",
]

webhook_url = os.environ.get("GREETER_WEBHOOK_URL")
if not webhook_url:
    raise RuntimeError("Environment variable GREETER_WEBHOOK_URL not set!")

device_noun = os.environ.get("GREETER_DEVICE_NOUN", "device")

sent = False
while not sent:
    print("Haven't sent greeting successfully yet, trying...")
    try:
        hostname = socket.gethostname()

        # Determine names to use to identify this machine.  If we're
        # running on Balena, then use the available environment
        # variables. Otherwise only report the hostname.
        on_balena = os.environ.get("BALENA")
        if on_balena:
            fleet_name = os.environ.get("BALENA_APP_NAME")
            device_name = os.environ.get("BALENA_DEVICE_NAME_AT_INIT")
        else:
            fleet_name = None
            device_name = hostname

        # Formulate greeting
        greeting = random.choice(greetings)
        fleet_description = f" of fleet *{fleet_name}*" if fleet_name else ""
        text = f"{greeting}! {device_noun.capitalize()} *{device_name}*{fleet_description} just came online."

        # Send request to Slack
        json = {"text": text}
        print(f"Sending JSON:\n{json}")
        response = requests.post(webhook_url, json=json)

        # Report the response received
        print("Response:")
        print(response)
        print(response.headers)
        print(response.text)

        sent = response.ok
    except Exception as e:
        print(e)
    finally:
        time.sleep(5.0)

print("Successfully sent greeting")
