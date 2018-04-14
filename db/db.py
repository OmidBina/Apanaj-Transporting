from peewee import *



def create_model(file_path, file_name):
    db = SqliteDatabase(file_path + file_name + '.db')

    class BaseModel(Model):
        class Meta:
            database = db

    class Message(BaseModel):
        message_id = IntegerField()
        message_text = TextField()
        modified_text = TextField(null=True)
        posted = BooleanField(default=False)
        message_type = TextField()
        file_name = CharField(null=True)
        file_size = IntegerField(null=True)

    db.connect()
    db.create_tables([Message])

    return Message


