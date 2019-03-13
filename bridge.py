#!/usr/bin/python3
import telegram.ext as tbot
import configparser
import argparse
import os
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def ExistingFile(path):
	if os.path.isfile(path):
		return path
	raise argparse.ArgumentTypeError("'{}' is not a path to a file".format(path))
	
parser=argparse.ArgumentParser(description="Bridging with bots!")
parser.add_argument("config",nargs="?",help="Location of config file.  Default: '%(default)s'",default='./config.ini',type=ExistingFile)
args=parser.parse_args()

config=configparser.ConfigParser()
config.read(args.config)

tConf=config['telegram']
TOKEN=tConf['token']
telegramOwner=tConf['owner'].lower() if 'owner' in tConf else None

updater=tbot.Updater(token=TOKEN)
dispatcher=updater.dispatcher

def ownerOnly(update,message):
	if telegramOwner is None or update.message.from_user.username.lower()==telegramOwner:
		update.message.reply_text(message)
	else:
		update.message.reply_text("i only take commands from master zangoose uwu")
def sayHi(bot,update):
	#print(update)
	#context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
	
	ownerOnly(update,"hewwo o3o")
	#print("Starting in:",update,context)
	#print("Chat id:",update.message.chat_id)

def getId(bots,update):
	ownerOnly(update,"Chat Id: "+str(update.message.chat_id))

def echo(bot,update):
	print(update)

hi_handler=tbot.CommandHandler('test', sayHi)
id_handler=tbot.CommandHandler('id', getId)
dispatcher.add_handler(hi_handler)
dispatcher.add_handler(id_handler)
#ispatcher.add_handler(tbot.MessageHandler(tbot.Filters.text, echo))

updater.start_polling()

