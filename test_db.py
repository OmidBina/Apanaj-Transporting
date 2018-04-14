from db.db import Message



for message in Message.select():
    print(message.message_text)
