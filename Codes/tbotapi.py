import config as cf
import requests


def runapi(**p):

    apiURL = f'https://api.telegram.org/bot{cf.telegram_bot}/sendMessage'

    try:
        response = requests.post(
            apiURL, json={
                'chat_id': p['chat_id'],
                'text': p['text'],
                'parse_mode': "html",
                'disable_web_page_preview': True
            }
        )
        return response.text
    except Exception as e:
        return e


def sendMessage(**p):
    return runapi(p)
