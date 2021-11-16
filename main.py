from telegram import (
    KeyboardButton, ChatMember, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, replykeyboardmarkup, replymarkup, user
)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from datetime import datetime
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update
import requests



my_token = "1955026889:AAFfjBn0PRv-z3-QA_yx2uG_e86XbvF8tho"

status = {
    1:"Halol",
    2:"Harom",
    3:"Mushbooh"
}
a = []
def start_command(update:Update,context:CallbackContext):
    button = [[KeyboardButton('Halol'),KeyboardButton('Harom')],[KeyboardButton('Mushbooh')]]
    btn = ReplyKeyboardMarkup(button,resize_keyboard=True)
    if update.message.from_user.id not in a:
        a.append(update.message.from_user.id)
        update.message.reply_html(text="Assaloma alaykum ",reply_markup=btn)
    else:
        update.message.reply_html(text="E code ni kiriting yoki quydagilarni birini tanlang ",reply_markup=btn)
    context.user_data['state'] = 'ecode'

def message_handler(update:Update,context:CallbackContext):
    msg = update.message.text
    res = requests.get(f"http://127.0.0.1:8000/json_ecode/{msg}")
    # res1 = requests.get(f"http://127.0.0.1:8000/json_name/{msg}")
    print(res)
    a = res.json()['data']
    if a['code'] ==200 and msg not in ["Halol", "Harom", "Mushbooh"]:
        text = f"<b>{a['ecode'] if a['ecode'] != '' else 'unknown' }</b>\n<b>{status[a['status']]}</b>\n{a['name']}\n<i>{a['desc']}</i>"   
        update.message.reply_html(text=text) 
    elif msg not in ["Halol", "Harom", "Mushbooh"] and a['code'] == 404:
        update.message.reply_html('<b>Siz qidirgan Ecode topilmadi</b>')

    elif msg == "Halol":
        data = requests.get('http://127.0.0.1:8000/json_status/1/')
        all = data.json()['data']
        print(all)
        text = ''
        if all != []:
            for a in all:
                text += f"<b>{a['ecode'] if a['ecode'] != '' else 'unknown' }</b>\n<b>{status[a['status']]}</b>\n{a['name']}\n<i>{a['desc']}</i>\n\n" 

        else:
            text = ('<b>afsus hech narsa topilamdi</b>')
        update.message.reply_html(text=text)
    elif msg == "Harom":
        data = requests.get('http://127.0.0.1:8000/json_status/2/')
        all = data.json()['data']
        text = ''
        if all != []:
            for a in all:
                text += f"<b>{a['ecode'] if a['ecode'] != '' else 'unknown' }</b>\n<b>{status[a['status']]}</b>\n{a['name']}\n<i>{a['desc']}</i>\n\n" 

        else:
            text = ('<b>afsus hech narsa topilamdi</b>')
        update.message.reply_html(text=text)
    elif msg == "Mushbooh":
        data = requests.get('http://127.0.0.1:8000/json_status/3/')
        all = data.json()['data']
        text = ''
        if all != []:
            for a in all:
                text += f"<b>{a['ecode'] if a['ecode'] != '' else 'unknown' }</b>\n<b>{status[a['status']]}</b>\n{a['name']}\n<i>{a['desc']}</i>\n\n" 

        else:
            text = ('<b>afsus hech narsa topilamdi</b>')
        update.message.reply_html(text=text)


    

    





def main():
    updater = Updater(my_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_command))
    # dispatcher.add_handler(CommandHandler("dashboard", admin_command))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    # dispatcher.add_handler(CallbackQueryHandler(callback_handler))
    # dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))    


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()