from db import Message
from filter import Filter

COUNTER = 0
for message in Message.select():
    clean_text = Filter.filter_message(message.message_text)

    message.message_text = clean_text
    message.save()
    COUNTER += 1
    print(COUNTER)
