from telethon import TelegramClient


api_id = 99515
api_hash = '0bbe352c1e6d93ddccbcd0445a7dde64'

client = TelegramClient('session_name', api_id, api_hash)
client.start()


def from_to_telegram(from_entity, to_entity, limit):
    for message in client.get_message_history(from_entity, limit=limit):
        client.send_message(to_entity, message=message.message, reply_to=None, parse_mode='md',
                            link_preview=True,
                            file=message.media, force_document=False)
        
        print("Message id: %s Forwarded." % (message.id))
