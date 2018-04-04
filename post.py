from db import Message

for message in Message.select():
    print(message.file_size)
