from telethon import TelegramClient
from telethon.tl.types import MessageService



api_id = 99515
api_hash = '0bbe352c1e6d93ddccbcd0445a7dde64'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
channel = client.get_entity('tabsir_afn')
for message in client.get_messages(channel, limit=1):
   print(message.id)
    #print(type(message.media) == MessageMediaPhoto)
    #client.send_message("iusthotornotbot", message=message.message, reply_to=None, parse_mode='md', link_preview=True,
                      #  file=message.media, force_document=False)

