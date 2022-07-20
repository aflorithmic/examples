from pprint import pprint
import json
import requests


API_KEY = "YOUR_API_KEY_HERE"
VOICE_NAME = "linda"
ENDPOINT_URL = "https://v1.api.audio/birdcache"

the_sentence = "Hi {{username|friend}}, welcome to {{city|tallinn}}. It is {{weather|rainy}} today. Have a great {{day|day}}"
audience = {
    "username": ["linda", "anne", "salih", "matt"],
    "city": ["istanbul", "tallinn", "london", "barcelona"],
    "weather": ["rainy", "sunny", "cloudy", "windy"],
    "day": ["monday", "friday", "sunday"],
}
mastering_sound_template = "openup"


def birdcache_v3_speech():
    r = requests.post(
        url=ENDPOINT_URL,
        headers={"x-api-key": API_KEY},
        data=json.dumps(
            {
                "voice": VOICE_NAME,
                "type": "speech",
                "text": the_sentence,
                "audience": audience,
            }
        ),
    )
    r = r.json()

    pprint("speech text files produced:")
    for req in r:
        print(req["text"])

    pprint("speech urls produced:")
    for req in r:
        print(req["text"] + " - " + (req["url"] if req["ready"] else "in progress"))


def birdcache_v3_mastering():
    r = requests.post(
        url=ENDPOINT_URL,
        headers={"x-api-key": API_KEY},
        data=json.dumps(
            {
                "voice": VOICE_NAME,
                "type": "mastering",
                "text": the_sentence,
                "audience": audience,
                "soundTemplate": mastering_sound_template,
            }
        ),
    )
    r = r.json()

    pprint("speech text files produced:")
    for req in r:
        print(req["text"])

    pprint("speech urls produced:")
    for req in r:
        print(req["text"] + " - " + (req["url"] if req["ready"] else "in progress"))


birdcache_v3_speech()
birdcache_v3_mastering()
