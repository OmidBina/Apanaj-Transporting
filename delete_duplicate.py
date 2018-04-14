from db import Message


COUNTER = 0
for message in Message.select().where(Message.message_type == "image"):
        for msg in Message.select().where(Message.message_text == message.message_text):
            if msg.message_type == "text":
                msg.delete_instance()
                COUNTER += 1
                print(COUNTER)
