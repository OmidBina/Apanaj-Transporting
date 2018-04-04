from telethon import TelegramClient
import time
import fire
from db import Message, ImageMessage, VideoMessgae

api_id = 99515
api_hash = '0bbe352c1e6d93ddccbcd0445a7dde64'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

FILESIZE = 5000
channel_id = "iustfuckers"
def do_job(entity_id, limit, msg, video, image):
    a = []
    for msg in client.get_message_history(entity_id, limit=limit):
        a.append(msg)

    a.reverse()
    for message in a:
        if msg:
            try:
                if message.media == None or message.media.webpage:
                    #client.send_message(channel_id, message=message.message, reply_to=None, link_preview=True, file=None, force_document=False)
                    Message.create(message_text=message.message)
            except AttributeError:
                pass
                #client.forward_messages('iusthotornotbot', message, from_peer=None)
        if video:
            try:
                if message.media.document:
                    if message.media.document.mime_type == "video/mp4":
                        #client.send_message(channel_id, message=message.message, reply_to=None, parse_mode='md', link_preview=True, file=message.media, force_document=False)
                        file_name = client.download_media(message, file="./files/"+str(message.media.document.id), progress_callback=None)
                        #file_name = "aa"
                        Message.create(message_text=str(message.message), file_size=message.media.document.size, file_name=file_name)
                        #if message.media.size < FILESIZE:
            except:
                pass

        if image:

            try:
                if message.media.photo:
                    file_name = client.download_media(message, file="./files/"+str(message.media.photo.id), progress_callback=None)
                    Message.create(message_text=message.message, file_name=file_name)
                    #client.send_message(channel_id, message=message.message, reply_to=None, parse_mode='md', link_preview=True, file=message.media, force_document=False)
            except:
                pass





do_job("NAZAR", 5, True, True, True)
