import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from pprint import pprint
import datetime
import requests
import json
import time
import smtplib

dizionario = {
    "comdex" : "https://api-comdex.cosmostation.io/v1/staking/validator/uptime/comdexvaloper1yyc7vmzy9w2g79gswz9cx845hh7l275cw7eg2r",
    "bitcanna" : "https://api-bitcanna.cosmostation.io/v1/staking/validator/uptime/bcnavaloper1yyc7vmzy9w2g79gswz9cx845hh7l275cetqeln",
    "cerberus" : "https://api-cerberus.cosmostation.io/v1/staking/validator/uptime/cerberusvaloper1yyc7vmzy9w2g79gswz9cx845hh7l275cnstkzq",
    "chihuahua" : "https://api-chihuahua.cosmostation.io/v1/staking/validator/uptime/chihuahuavaloper1yyc7vmzy9w2g79gswz9cx845hh7l275c2yvtlt",
    "evmos" : "https://api-evmos.cosmostation.io/v1/staking/validator/uptime/evmosvaloper1d7uejj7he40g6g999dlpfg5egeq9jvkmlzvsjn"
}



TOKEN='5311084919:AAHYLqT1mNg8evs8DAho8rLXpuTuSfSuIiI'

#sticker=open('pollice.jpg','rb')

def on_chat_message(msg):
    
    content_type,chat_type,chat_id=telepot.glance(msg)
    if content_type=='text':
        name=msg['from']['first_name']
        txt=msg['text']
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                     [InlineKeyboardButton(text='Evmos', callback_data='evmos'),
                     InlineKeyboardButton(text='Comdex', callback_data='comdex')],
                     [InlineKeyboardButton(text='BitCanna', callback_data='bitcanna'),
                     InlineKeyboardButton(text='Cerberus', callback_data='cerberus'),
                     InlineKeyboardButton(text='Chihuahua', callback_data='chihuahua')],
                 ])
        bot.sendMessage(chat_id,'🇮🇹 Benvenuto *' + str(name) + '* nel bot di monitoraggio ufficiale di NodeOf Cosmonauts🧑🏼‍🚀, seleziona la chain che vuoi controllare. \n\n🇪🇺 Welcome *' + name + '* to NodeOf Cosmonauts🧑🏼‍🚀 official tracking bot, select the chain you want to check. \n', reply_markup=keyboard, parse_mode='Markdown')
        

def on_callback_query(msg):
    query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, chat_id, query_data)
    if query_data=='evmos':
        ric = requests.get(dizionario["evmos"])

        risposta = json.loads(str(ric.text))

        uptime = risposta['uptime']

        contenuto=""

        if(len(uptime)> 0):
            for missed in uptime:
                del(missed['id'])
                data = datetime.datetime.strptime(str(missed['timestamp']).split('.')[0].replace("T", " "), "%Y-%m-%d %H:%M:%S")
                data = data + datetime.timedelta(hours=2)
                contenuto = contenuto + "Height: "+ str(missed['height']) + "\t" + "Date: " + data.strftime("%Y-%m-%d %H:%M:%S") + "\n"

            oggetto = "Subject: Perdita di "+ str(len(uptime)) +" Blocchi " + "evmos".upper() +"\n\n"
            messaggio = oggetto + contenuto

            bot.sendMessage(chat_id, messaggio)
        else:
            bot.sendMessage(chat_id, "Nessuna blocco perso: EVMOS")
    elif query_data=='comdex':
        ric = requests.get(dizionario["comdex"])

        risposta = json.loads(str(ric.text))

        uptime = risposta['uptime']

        contenuto=""

        if(len(uptime)> 0):
            for missed in uptime:
                del(missed['id'])
                data = datetime.datetime.strptime(str(missed['timestamp']).split('.')[0].replace("T", " "), "%Y-%m-%d %H:%M:%S")
                data = data + datetime.timedelta(hours=2)
                contenuto = contenuto + "Height: "+ str(missed['height']) + "\t" + "Date: " + data.strftime("%Y-%m-%d %H:%M:%S") + "\n"

            oggetto = "Subject: Perdita di "+ str(len(uptime)) +" Blocchi " + "comdex".upper() +"\n\n"
            messaggio = oggetto + contenuto

            bot.sendMessage(chat_id, messaggio)
        else:
            bot.sendMessage(chat_id, "Nessuna blocco perso: COMDEX")
    elif query_data=='bitcanna':
        ric = requests.get(dizionario["bitcanna"])

        risposta = json.loads(str(ric.text))

        uptime = risposta['uptime']

        contenuto=""

        if(len(uptime)> 0):
            for missed in uptime:
                del(missed['id'])
                data = datetime.datetime.strptime(str(missed['timestamp']).split('.')[0].replace("T", " "), "%Y-%m-%d %H:%M:%S")
                data = data + datetime.timedelta(hours=2)
                contenuto = contenuto + "Height: "+ str(missed['height']) + "\t" + "Date: " + data.strftime("%Y-%m-%d %H:%M:%S") + "\n"

            oggetto = "Subject: Perdita di "+ str(len(uptime)) +" Blocchi " + "bitcanna".upper() +"\n\n"
            messaggio = oggetto + contenuto

            bot.sendMessage(chat_id, messaggio)
        else:
            bot.sendMessage(chat_id, "Nessuna blocco perso: BITCANNA")
    elif query_data=='cerberus':
        ric = requests.get(dizionario["cerberus"])

        risposta = json.loads(str(ric.text))

        uptime = risposta['uptime']

        contenuto=""

        if(len(uptime)> 0):
            for missed in uptime:
                del(missed['id'])
                data = datetime.datetime.strptime(str(missed['timestamp']).split('.')[0].replace("T", " "), "%Y-%m-%d %H:%M:%S")
                data = data + datetime.timedelta(hours=2)
                contenuto = contenuto + "Height: "+ str(missed['height']) + "\t" + "Date: " + data.strftime("%Y-%m-%d %H:%M:%S") + "\n"

            oggetto = "Subject: Perdita di "+ str(len(uptime)) +" Blocchi " + "cerberus".upper() +"\n\n"
            messaggio = oggetto + contenuto

            bot.sendMessage(chat_id, messaggio)
        else:
            bot.sendMessage(chat_id, "Nessuna blocco perso: CERBERUS")
    elif query_data=='chihuahua':
        ric = requests.get(dizionario["chihuahua"])

        risposta = json.loads(str(ric.text))

        uptime = risposta['uptime']

        contenuto=""

        if(len(uptime)> 0):
            for missed in uptime:
                del(missed['id'])
                data = datetime.datetime.strptime(str(missed['timestamp']).split('.')[0].replace("T", " "), "%Y-%m-%d %H:%M:%S")
                data = data + datetime.timedelta(hours=2)
                contenuto = contenuto + "Height: "+ str(missed['height']) + "\t" + "Date: " + data.strftime("%Y-%m-%d %H:%M:%S") + "\n"

            oggetto = "Subject: Perdita di "+ str(len(uptime)) +" Blocchi " + "chihuahua".upper() +"\n\n"
            messaggio = oggetto + contenuto

            bot.sendMessage(chat_id, messaggio)
        else:
            bot.sendMessage(chat_id, "Nessuna blocco perso: CHIHUAHUA")

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
				  'callback_query': on_callback_query}).run_as_thread() 
print('Listening ...')

while 1:
    time.sleep(0.1)