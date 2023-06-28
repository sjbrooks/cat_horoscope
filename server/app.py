"""Routes for cat horoscope extension."""

import requests

import openai
from flask import Flask, request
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension

import secrets

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = secrets.FLASK_SECRET_KEY
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['TESTING'] = True
toolbar = DebugToolbarExtension(app)

HOROSCOPE_API_BASE_URL = "https://ohmanda.com/api/horoscope/"
openai.api_key = secrets.CHAT_GPT_API_KEY


@app.route("/cat_horoscope", methods=["GET"])
def get_horoscope():
    """Returns horoscope text."""
    sun_sign: str = request.args.get("sun_sign", "pisces")
    request_url: str = f"{HOROSCOPE_API_BASE_URL}{sun_sign}"
    response = requests.get(request_url, timeout=10)
    horoscope_text: str = response.json()["horoscope"]
    print(horoscope_text)

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Rewrite this horoscope with cat humor and puns: {horoscope_text}"},
            ]
    )
    cat_horoscope: str = chat_completion["choices"][0]["message"]["content"]
    print(horoscope_text)
    return {
        "cat_horoscope": cat_horoscope,
    }
