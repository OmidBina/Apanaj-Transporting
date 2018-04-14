from peewee import *


db = SqliteDatabase('messages.db')


class BaseModel(Model):
    class Meta:
        database = db


class Message(BaseModel):
    message_id = IntegerField()
    message_text = TextField()
    modified_text = TextField()
    posted = BooleanField(default=False)
    message_type = TextField()
    file_name = CharField(null = True)
    file_size = IntegerField(null = True)


class ImageMessage(BaseModel):
    file_name = CharField()
    message_text = TextField()


class VideoMessgae(BaseModel):
    file_name = CharField()
    file_size = IntegerField()
    message_text = TextField(null=True)


db.connect()

db.create_tables([Message])
