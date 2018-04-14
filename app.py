from telethon import TelegramClient
import time
import fire
from filter import Filter
from db import Message, ImageMessage, VideoMessgae

api_id = 99515
api_hash = '0bbe352c1e6d93ddccbcd0445a7dde64'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
COUNTER = 0
FILESIZE = 5000

def do_job(entity_id, limit, msg, video, image, music):

    a = []
    for msg in client.get_message_history(entity_id, limit=limit):
        a.append(msg)

    a.reverse()
    for message in a:

        if msg:
            try:
                if message.media == None or message.media.webpage:
                    #client.send_message(channel_id, message=message.message, reply_to=None, link_preview=True, file=None, force_document=False)
                    #msg = Message.get(Message.message_id == message.id)

                    #Message.create(message_id=message.id, message_text=Filter.filter_message(message.message))
                    handle_messages(message, False, False, False)
                    #Message.create(message_id=message.id, message_text=Filter.filter_message(message.message))
            except AttributeError:
                pass
                #client.forward_messages('iusthotornotbot', message, from_peer=None)
        if video:
            try:
                if message.media.document:
                    if message.media.document.mime_type == "video/mp4":
                        #client.send_message(channel_id, message=message.message, reply_to=None, parse_mode='md', link_preview=True, file=message.media, force_document=False)
                        #file_name = client.download_media(message, file="./files/"+str(message.media.document.id), progress_callback=None)
                        #file_name = "aa"
                        #msg, created = Message.get_or_create(message_id=message.id, message_text=str(message.message), file_size=message.media.document.size, file_name=file_name)
                        #if message.media.size < FILESIZE:
                        handle_messages(message, False, True, False)
            except:
                pass

        if image:
            try:
                if message.media.photo:
                    #file_name = client.download_media(message, file="./files/"+str(message.media.photo.id), progress_callback=None)
                    #msg, created = Message.get_or_create(message_id=message.id, message_text=message.message, file_name=file_name)
                    #client.send_message(channel_id, message=message.message, reply_to=None, parse_mode='md', link_preview=True, file=message.media, force_document=False)
                    handle_messages(message, True, False, False)
            except:
                pass
        if music:
            try:
                if message.media.document.mime_type == 'audio/mp3' or message.media.document.mime_type == 'audio/mpeg' or message.media.document.mime_type =='audio/mp4':
                    #file_name = client.download_media(message, file="./files/"+str(message.media.photo.id), progress_callback=None)
                    #msg, created = Message.get_or_create(message_id=message.id, message_text=message.message, file_name=file_name)
                    #client.send_message(channel_id, message=message.message, reply_to=None, parse_mode='md', link_preview=True, file=message.media, force_document=False)
                    handle_messages(message, False, False, True)
            except:
                pass








def handle_messages(message, image, video, music):
    if Message.select().where(Message.message_id == message.id):
        print("Message with %s is Already Saved." % (message.id))
    else:
        if video:
            if message.media.document.size < 5242880:
                file_name = client.download_media(message, file="./files/"+str(message.id), progress_callback=None)
                Message.create(message_id=message.id, message_text=message.message, message_type="video", file_size=message.media.document.size, file_name=file_name)

        if image:
            file_name = client.download_media(message, file="./files/"+str(message.id), progress_callback=None)
            Message.create(message_id=message.id, message_text=message.message, message_type="image", file_size=None, file_name=file_name)

        if music:
            file_name = client.download_media(message, file="./files/"+str(message.id), progress_callback=None)
            Message.create(message_id=message.id, message_text=message.message, message_type="msuic", file_size=message.media.document.size, file_name=file_name)

        else:
            Message.create(message_id=message.id, message_text=message.message, message_type="text", file_size=None, file_name=None)
    global COUNTER
    COUNTER += 1
    print("%d: Message id: %d Saved." % (COUNTER, message.id))

do_job("khamenei_reyhaneh", 2821, True, True, True, True)


#msg = Message.get(Message.message_id == 51768)
