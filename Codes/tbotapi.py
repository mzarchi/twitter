import config as cf
import requests


def runapi(**args):

    apiURL = f"https://api.telegram.org/bot{cf.telegram_bot}/{args['method']}"

    try:
        response = requests.post(
            apiURL, json=args['djson']
        )
        return response.text
    except Exception as e:
        return e


def send_message(**p):
    return runapi(
        method="sendMessage",
        djson={
            'chat_id': p['chat_id'],
            'text': p['text'],
            'parse_mode': "html",
            'disable_web_page_preview': True
        }
    )
