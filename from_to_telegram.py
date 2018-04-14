from telethon import TelegramClient




api_id = 99515
api_hash = '0bbe352c1e6d93ddccbcd0445a7dde64'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

for message in client.get_message_history("zeitgeistsystem", limit=10):

    print(message.id)
    client.send_message("iusthotornotbot", message=message.message, reply_to=None, parse_mode='md', link_preview=True,
                        file=message.media, force_document=False)

