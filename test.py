from telethon import TelegramClient
import time
import fire


api_id = 99515
api_hash = '0bbe352c1e6d93ddccbcd0445a7dde64'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

for message in client.get_message_history("NAZAR", limit=5):
    print(message)
