from db.db import create_model

Message = create_model("../user_data/zeitgeistsystem/", "messages")
COUNTER = 0
for message in Message.select():
    #clean_text = Filter.filter_message(message.message_text)
    print(message.file_name)
    #message.modified_text = clean_text
    #message.save()
    #COUNTER += 1
   # print(COUNTER)
