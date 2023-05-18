from telegram.ext import Updater, CommandHandler

def greet_user(update, context):
    print('Вызван /start')

def main():
    mybot = Updater("6288351373:AAE9nTQUv-uKYq_3SNiHACQNSTH-u4ipZXw", use_context = True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    mybot.start_polling()
    mybot.idle()

main()