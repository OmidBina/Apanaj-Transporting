from telethon import TelegramClient
import time
import fire


api_id = 99515
api_hash = '0bbe352c1e6d93ddccbcd0445a7dde64'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

FILESIZE = 100000000

def do_job(entity_id, limit, msg, video, image):
    for message in client.get_message_history(entity_id, limit=limit):
        if msg:
            if message.media == None:
                client.send_message("iusthotornotbot", message=message.message, reply_to=None, parse_mode='md', link_preview=True, file="aa.jpg", force_document=False)
                #client.forward_messages('iusthotornotbot', message, from_peer=None)
        if video:
            try:
                if message.media.document.mime_type == "video/mp4":
                    client.send_message("iusthotornotbot", message=message.message, reply_to=None, parse_mode='md', link_preview=True, file=message.media, force_document=False)
                    print(message)
                    #if message.media.size < FILESIZE:

            except AttributeError:
                pass
        if image:
            try:
                if message.media.photo:
                    client.send_message("iusthotornotbot", message=message.message, reply_to=None, parse_mode='md', link_preview=True, file=message.media, force_document=False)
            except AttributeError:
                pass



do_job("NAZAR", 5, True, True, True)
