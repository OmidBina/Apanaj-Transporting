import pyautogui as pg
import sys

sys.path.append('../db/')
from db import create_model
import os
from time import sleep
import pyperclip
Message = create_model("../user_data/zeitgeistsystem/", "messages")
SMALL_DELAY = 0.75
MEDIUM_DELAY = 1
file_pathhh = "C:\\Users\\Apanaj\\Desktop\\transporting\\user_data\\zeitgeistsystem\\files\\"

def post_image(file_name, message_text):
    pg.click(940, 708)
    sleep(MEDIUM_DELAY)

    pg.typewrite(file_pathhh + file_name[24:])
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
    pg.click(275, 709)
    pyperclip.copy(message_text)
    sleep(SMALL_DELAY)
    pg.hotkey("ctrl", "v")
    sleep(SMALL_DELAY)
    pg.press("enter")


def post_video(message):
    # rename_file(file_name[8:])
    pg.click(940, 708)
    sleep(MEDIUM_DELAY)
    pg.typewrite(file_pathhh + message.file_name[24:])
    sleep(SMALL_DELAY)
    pg.click(513, 439)
    sleep(SMALL_DELAY)
    #pg.click(566, 347)
    sleep(SMALL_DELAY)
    #sleep(120)
    post_text(message.message_text)




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
        post_image(message.file_name, message.modified_text)

    if message.message_type == "text":
        post_text(message.modified_text)

    message.posted = True
    message.save()
    sleep(1)
