import json
import requests
from flask_babel import _
from flask import current_app

def translate(text, language_input, language_output):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&from=' + language_input + '&to=' + language_output
    constructed_url = base_url + path + params
    headers = auth
    body = [{ 'text' : text }]
    response = requests.post(constructed_url, headers=headers, json=body)
    if response.status_code != 200:
        return _('Error: translation service failed.')
    return response.json()[0]['translations'][0]['text']