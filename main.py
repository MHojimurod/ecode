from telegram import (
    KeyboardButton, ReplyKeyboardMarkup, InlineQueryResultArticle
)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

from telegram.ext.callbackcontext import CallbackContext
from telegram.inline.inputmessagecontent import InputMessageContent
from telegram.inline.inputtextmessagecontent import InputTextMessageContent
from telegram.update import Update
import requests



my_token = "2112456432:AAHf4Wz7LR0rZiqZxReJQrhUUsLitTMw-vk"

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
    msg = msg.strip().lower().replace(" ", "")
    res = requests.get(f"http://157.245.221.46/json_ecode/{msg}")
    a = res.json()['data']
    print(a)
    print(msg)

    if a['code'] == 200 and msg not in ["halol", "harom", "muboh"]:
        text = f"<b>{a['ecode'] if a['ecode'] != '' else 'unknown' }</b>\n<b>{status[a['status']]}</b>\n{a['name']}\n<i>{a['desc']}</i>"
        update.message.reply_html(text=text) 
    elif msg not in ["halol", "harom", "muboh"] and a['code'] == 404:
        update.message.reply_html('<b>Siz qidirgan Ecode topilmadi</b>')

    elif msg == "halol":
        data = requests.get('http://157.245.221.46/json_status/1/')
        all = data.json()['data']
        print(all)
        text = ''
        if all != []:
            for a in all:
                text += f"<b>{a['ecode'] if a['ecode'] != '' else 'unknown' }</b>\n<b>{status[a['status']]}</b>\n{a['name']}\n<i>{a['desc']}</i>\n\n" 

        else:
            text = ('<b>afsus hech narsa topilamdi</b>')
        update.message.reply_html(text=text)
    elif msg == "harom":
        data = requests.get('http://157.245.221.46/json_status/2/')
        all = data.json()['data']
        text = ''
        if all != []:
            for a in all:
                text += f"<b>{ a['ecode'] if a['ecode'] != '' else 'unknown' }</b>\n<b>{status[a['status']]}</b>\n{a['name']}\n<i>{a['desc']}</i>\n\n" 
        else:
            text = ('<b>afsus hech narsa topilamdi</b>')
        update.message.reply_html(text=text)
    elif msg == "muboh":
        data = requests.get('http://157.245.221.46/json_status/3/')
        all = data.json()['data']
        text = ''
        if all != []:
            for a in all:
                text += f"<b>{a['ecode'] if a['ecode'] != '' else 'unknown' }</b>\n<b>{status[a['status']]}</b>\n{a['name']}\n<i>{a['desc']}</i>\n\n" 
        else:
            text = ('<b>afsus hech narsa topilamdi</b>')
        update.message.reply_html(text=text)
    else:
        start_command(update,context)

def inline_handler(update:Update, context:CallbackContext):
    query = update.inline_query.query
    query = query.strip().lower()
    res = requests.get(f"http://157.245.221.46/json_data/")
    results = []
    for i in res.json()['data']:
        if query in i['ecode'].lower() or query in i['name'].lower():
            results.append(InlineQueryResultArticle(
                id=i['id'],
                    title=f'{i["ecode"]} | {i["name"]} | {status[i["status"]]}',
                    input_message_content=InputTextMessageContent(
                        message_text=f'<b>{i["ecode"]}</b>\n<b>{status[i["status"]]}</b>\n<b><i>{i["name"]}</i></b>\n{i["desc"]}',
                    parse_mode="HTML"),
                ))
    

    update.inline_query.answer(
        results=results,
        cache_time=10,
    )

    





def main():
    updater = Updater(my_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(InlineQueryHandler(inline_handler))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()