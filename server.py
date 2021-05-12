from bot import telegram_chatbot
from urllib.parse import urlparse, parse_qs
from urllib import request
import json

bot = telegram_chatbot("config.cfg")


def valid_url(e):
    try:
        url_ = "https://www.youtube.com/oembed?format=json&url=" + e
        response = request.urlopen(url_)
        page_source = response.read()
        str_ = str(page_source.decode('utf-8'))
        dict_ = json.loads(str_)
        return (dict_['thumbnail_url'])
    except:
        return None

def make_reply(msg,chat_id):

    if msg is not None:
        if msg == '/start' or msg == '/help':
            bot.send_message('Welcome to Youtube Thumbnail Download bot . Send a youtube video url ',chat_id)
        elif msg == '/contact':
            bot.send_message("Send your query to @Contact_mg_bot",chat_id)
        elif msg == '/web':
            bot.send_message("visit : https//:mastergeniusweb.000webhostapp.com/",chat_id)
        else:
            if valid_url(msg) is not None:
                    thumbnailurl= valid_url(msg)
                    bot.sendImageRemoteFile(chat_id,thumbnailurl)
            else:
                bot.send_message('Please Enter a valid youtube video url',chat_id)

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            try:
               from_ = item["message"]["from"]["id"]
               reply = make_reply(message,from_)
            except:
                   pass
