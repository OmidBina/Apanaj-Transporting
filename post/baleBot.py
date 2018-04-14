"""Simple hear with your bot"""

import asyncio

from balebot.filters import *
from balebot.models.messages import TextMessage
from balebot.updater import Updater

# A token you give from BotFather when you create your bot set below
updater = Updater(token="e20d43ca38ff6095acbf4a83fcc92f6a635f382f")
# Define dispatcher
dispatcher = updater.dispatcher


# Both of success and failure functions are optional
def success(result, user_data):
    print("success : ", result)
    print(user_data)


def failure(result, user_data):
    print("failure : ", result)
    print(user_data)


# hear function
@dispatcher.message_handler(filters=DefaultFilter())  # filter text the client enter to bot
def hear(bot, update):
    print("hiiiiiiiiiii")

    message = TextMessage('Hello')
    user_peer = update.get_effective_user()
    bot.send_message(message, user_peer)


# Run the bot!
updater.run()
