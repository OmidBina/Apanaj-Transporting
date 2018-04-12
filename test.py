from telethon import TelegramClient
import time
import fire


api_id = 99515
api_hash = '0bbe352c1e6d93ddccbcd0445a7dde64'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
a = []
for msg in client.get_message_history("zeitgeistsystem", limit=1):
    try:
        print(msg.id)
        #print(client.download_media(msg, file="./files/"+str(msg.media.document.id), progress_callback=None))
    except:
        pass
