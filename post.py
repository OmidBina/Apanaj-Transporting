from db import Message
from telethon import TelegramClient


api_id = 99515
api_hash = '0bbe352c1e6d93ddccbcd0445a7dde64'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
COUNTER = 0
for message in Message.select():
    print(message.file_size)
    client.send_message("iustfuckers", message=message.message_text, reply_to=None, link_preview=True, file=message.file_name, force_document=False)

    print(COUNTER)
    COUNTER += 1
