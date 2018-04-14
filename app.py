from telethon import TelegramClient
#from filter import Filter
from tqdm import tqdm
from db.db import create_model
from telethon.tl.types import MessageMediaPhoto
from telethon.tl.types import MessageMediaDocument
from telethon.tl.types import MessageService
import fire

Message = None

api_id = 99515
api_hash = '0bbe352c1e6d93ddccbcd0445a7dde64'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
COUNTER = 0
FILE_SIZE = 9000000000
ENTITY_NAME = None
USER_DATA_PATH = None


def do_job(entity_id, limit, text, video, image, music):

    reverse_messages = []
    for msg in client.get_messages(entity_id, limit=limit):
        if type(msg) != MessageService:
            reverse_messages.append(msg)

    reverse_messages.reverse()

    for message in reverse_messages:
        if text:
            if message.media == None or hasattr(message.media, 'webpage'):
                #client.send_message(channel_id, message=message.message, reply_to=None, link_preview=True, file=None, force_document=False)
                #msg = Message.get(Message.message_id == message.id)

                #Message.create(message_id=message.id, message_text=Filter.filter_message(message.message))
                handle_messages(message, True, False, False, False)
                #Message.create(message_id=message.id, message_text=Filter.filter_message(message.message))

        if video:
            if type(message.media) == MessageMediaDocument:
                if message.media.document.mime_type == "video/mp4":
                    #client.send_message(channel_id, message=message.message, reply_to=None, parse_mode='md', link_preview=True, file=message.media, force_document=False)
                    #file_name = client.download_media(message, file="./files/"+str(message.media.document.id), progress_callback=None)
                    #file_name = "aa"
                    #msg, created = Message.get_or_create(message_id=message.id, message_text=str(message.message), file_size=message.media.document.size, file_name=file_name)
                    #if message.media.size < FILESIZE:
                    handle_messages(message, False, False, True, False)


        if image:
            if type(message.media) == MessageMediaPhoto:
                #file_name = client.download_media(message, file="./files/"+str(message.media.photo.id), progress_callback=None)
                #msg, created = Message.get_or_create(message_id=message.id, message_text=message.message, file_name=file_name)
                #client.send_message(channel_id, message=message.message, reply_to=None, parse_mode='md', link_preview=True, file=message.media, force_document=False)
                handle_messages(message, False, True, False, False)

        if music:
            if type(message.media) == MessageMediaDocument:
                if message.media.document.mime_type == 'audio/mp3' or message.media.document.mime_type == 'audio/mpeg' or message.media.document.mime_type =='audio/mp4':
                    #file_name = client.download_media(message, file="./files/"+str(message.media.photo.id), progress_callback=None)
                    #msg, created = Message.get_or_create(message_id=message.id, message_text=message.message, file_name=file_name)
                    #client.send_message(channel_id, message=message.message, reply_to=None, parse_mode='md', link_preview=True, file=message.media, force_document=False)
                    handle_messages(message, False, False, False, True)


def show_download_process(recv, totlal):
    print(recv)


def save_to_db(message, text, image, video, music):
    if Message.select().where(Message.message_id == message.id):
        print("Message with %s is Already Saved." % (message.id))
    else:
        if video:
            if message.media.document.size < FILE_SIZE:
                file_name = client.download_media(message, file=USER_DATA_PATH+str(message.id), progress_callback=show_download_process)
                Message.create(message_id=message.id, message_text=message.message, message_type="video", file_size=message.media.document.size, file_name=file_name)

        if image:
            file_name = client.download_media(message, file=USER_DATA_PATH+str(message.id), progress_callback=show_download_process)
            Message.create(message_id=message.id, message_text=message.message, message_type="image", file_size=None, file_name=file_name)

        if music:
            file_name = client.download_media(message, file=USER_DATA_PATH+str(message.id), progress_callback=None)
            Message.create(message_id=message.id, message_text=message.message, message_type="msuic", file_size=message.media.document.size, file_name=file_name)

        if text:
            Message.create(message_id=message.id, message_text=message.message, message_type="text", file_size=None, file_name=None)
        global COUNTER
        COUNTER += 1
        print("%d: Message id: %d Saved." % (COUNTER, message.id))


def to_new_channel(channel_id, text, message, image, video, music):
    if video:
        client.send_message(channel_id, message=message.message, reply_to=None, parse_mode='md', link_preview=True,
                            file=message.media, force_document=False)
    if image:
        client.send_message(channel_id, message=message.message, reply_to=None, parse_mode='md', link_preview=True,
                            file=message.media, force_document=False)
    if music:
        client.send_message(channel_id, message=message.message, reply_to=None, parse_mode='md', link_preview=True,
                            file=message.media, force_document=False)
    if text:
        client.send_message(channel_id, message=message.message, reply_to=None, link_preview=True, file=None,
                            force_document=False)


def handle_messages(message, text, image, video, music):
    save_to_db(message, text, image, video, music)
    #to_new_channel("iusthotornotbot", text, message, image, video, music)




class App(object):

  def save(self, from_entity, limit):
      ENTITY_NAME = from_entity
      global  USER_DATA_PATH
      USER_DATA_PATH = "./user_data/" + from_entity + "/files/"
      global Message
      Message = create_model("./user_data/" + from_entity + "/", from_entity)
      entity = client.get_entity(from_entity)
      do_job(entity, limit, True, True, True, True)


if __name__ == '__main__':
  fire.Fire(App)
