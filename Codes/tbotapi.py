import config as cf
import requests


def runapi(chat_id, text):

    apiURL = f'https://api.telegram.org/bot{cf.telegram_bot}/sendMessage'

    try:
        response = requests.post(
            apiURL, json={
                'chat_id': chat_id,
                'text': text,
                'parse_mode': "html",
                'disable_web_page_preview': True
            }
        )
        return response.text
    except Exception as e:
        return e


def send_message(**p):
    return runapi(p['chat_id'], p['text'])
