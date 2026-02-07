import telebot
from telebot.types import Message
token = "7198581184:AAGpgOpE71Ran5JfZVimYK8M_GbTeflDUu8"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m:Message):
    bot.send_message(m.chat.id, "Бот будет повторять твои сообщения! Попробуй что-то написать")

@bot.message_handler(func=lambda message: True)
def echo(m:Message):
    bot.reply_to(m, m.text)

@bot.message_handler(commands=["git"])
def command_git(m:Message):
    bot.send_message(m.chat.id, "Этот бот добавлен в github")



bot.infinity_polling()
