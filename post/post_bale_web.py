import pyautogui as pg
from db.db import Message
import os
from time import sleep
import pyperclip

SMALL_DELAY = 1
MEDIUM_DELAY = 1.5


def post_image(file_name, message_text):
    pg.click(194, 697)
    sleep(MEDIUM_DELAY)
    pg.typewrite(file_name[8:])
    sleep(SMALL_DELAY)
    pg.click(513, 439)
    sleep(SMALL_DELAY)
    #print(message_text)
    pyperclip.copy(message_text)
    sleep(SMALL_DELAY)
    pg.hotkey("ctrl", "v")
    #pg.typewrite(file_name, interval=0.25)
    sleep(MEDIUM_DELAY)
    pg.press("enter")

def post_text(message_text):
    pg.click(259, 605)
    pyperclip.copy(message_text)
    sleep(SMALL_DELAY)
    pg.hotkey("ctrl", "v")
    sleep(SMALL_DELAY)
    pg.press("enter")


def post_video(message):
    # rename_file(file_name[8:])
    pg.click(194, 697)
    sleep(MEDIUM_DELAY)
    pg.typewrite(message.file_name[8:])
    sleep(SMALL_DELAY)
    pg.click(513, 439)
    sleep(SMALL_DELAY)
    pg.click(566, 347)
    sleep(SMALL_DELAY)
    sleep(3)
    #post_text(message.message_text)




def rename_file(file_name):
    base_path = "C:\\Users\\Zakeri\\Desktop\\Tele\\files\\"
    full_path = base_path + file_name
    base = os.path.splitext(full_path)[0]
    os.rename(full_path, base + ".gif")


for message in Message.select().where(Message.posted == False):
    #sleep(2)
    if message.message_type == "video":
        # Vide
        post_video(message)
    if message.message_type == "music":
        # Vide
        post_video(message)
    if message.message_type == "image":
        # Photo
        post_image(message.file_name, message.message_text)

    if message.message_type == "text":
        post_text(message.message_text)

    message.posted = True
    message.save()
    #sleep(2)
