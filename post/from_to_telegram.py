from telethon import TelegramClient
from utils.filter import Filter
from telethon.tl.types import MessageService
api_id = 99515
api_hash = '0bbe352c1e6d93ddccbcd0445a7dde64'

client = TelegramClient('session_name', api_id, api_hash)
client.start()


def from_to_telegram(from_entity, to_entity, limit):
    reverse_messages = []
    for msg in client.get_messages(from_entity, limit=limit):
        if msg.id > 570:
            reverse_messages.append(msg)


    reverse_messages.reverse()
    for message in reverse_messages:
        if type(message) != MessageService:
            if hasattr(message, 'media'):

                if hasattr(message.media, 'webpage'):
                    client.send_message(to_entity, message=Filter.filter_message(message.message), reply_to=None,
                                        parse_mode='md',
                                        link_preview=True,
                                        file=None, force_document=False)
                else:
                    client.send_message(to_entity, message=Filter.filter_message(message.message), reply_to=None,
                                        parse_mode='md',
                                        link_preview=True,
                                        file=message.media, force_document=False)
                print("Message id: %s Forwarded." % (message.id))
        else:
            print("--------Messave Service")




channel = client.get_entity('https://t.me/joinchat/AAAAAD6N4PVREVsXoHiLOw')
#print(channel)
from_to_telegram(channel, "shams_test1", None)
