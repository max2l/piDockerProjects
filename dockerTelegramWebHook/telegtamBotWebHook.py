#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cherrypy, time, configparser, telebot, subprocess, os, sys, transmissionrpc

config = configparser.RawConfigParser()
config.read('/etc/telegramBot.cfg')
tempDirectory = config.get('telegram','tempDirectory')
transmissionPort = config.getint('transmission','transmissionPort')
transmissionHost = config.get('transmission','transmissionHost')
transmissionUsername = config.get('transmission','transmissionUsername')
transmissionPassword = config.get('transmission','transmissionPassword')
tempDirectory = '/tmp/'

BOT_TOKEN = config.get('telegram','botTelegramToken')
idAdminClient = config.getint('telegram','idAdmin')

helpMeaasge = """
/help, /start           Print this mesage.
/listTor                List all torrent files.
/delTor                 Delete torrent files use id.
/fileTor                Download attaced torent file.
/vpnon                  Start Open VPN Server.
/vpnoff                 Stop Open VPN Server.
/rtb                    Reload Telegram Boot script.
"""

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start","help"])
def reply_to(message):
    if message.chat.id == idAdminClient:
        bot.send_message(message.chat.id, helpMeaasge)
    else:
        bot.send_message(message.chat.id, "You are not authorized user!")
        bot.send_message(idAdminClient, "Warninig!! User: " + str(message.chat.id) + " Attempt to access resources" )

@bot.message_handler(commands=["listTor","listtor","ListTor"])
def list_torent(message):
    listTorrents = ''
    try:
        tc = transmissionrpc.Client(transmissionHost, transmissionPort, user=transmissionUsername, password=transmissionPassword)
        for torrent in tc.get_torrents():
            listTorrents = listTorrents + (str(torrent.id) + "\t" + torrent.status +	"\t" + torrent.name + "\n")
        del tc

        bot.send_message(message.chat.id, listTorrents)
    except Exception as e:
        bot.send_message(message.chat.id, "Error: " + str(e) + ". Please try leater.")

@bot.message_handler(commands=["delTor","DelTor","deltor"])
def del_tor(message):
    msg = bot.send_message(message.chat.id, "Please enter id torent for delete.")
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    try:
        idTorrent = int(message.text)
        tc = transmissionrpc.Client(transmissionHost, transmissionPort, user=transmissionUsername, password=transmissionPassword)
        tc.remove(delete_data=True, ids=idTorrent)
    except Exception as e:
        bot.send_message(message.chat.id, "Torrent did not delete. " + str(e))
        return ''

    bot.send_message(message.chat.id, "Torren delete successfully." )

@bot.message_handler(commands=["fileTor","filetor","TileTor"])
def file_tor(message):
    msg = bot.send_message(message.chat.id, "Please attache torrent file.")
    bot.register_next_step_handler(msg, process_file_tor_step)

def process_file_tor_step(message):
    if message.document.mime_type == 'application/x-bittorrent':
        try:
            chat_id = message.chat.id

            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            src = tempDirectory + message.document.file_name;
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)


            try:
                tc = transmissionrpc.Client(transmissionHost, transmissionPort, user=transmissionUsername, password=transmissionPassword)
                tc.add_torrent(src)
                os.remove(src)
                bot.send_message(message.chat.id,"Файлы скачиваются.")
            except Exception as e:
                bot.send_message(message.chat.id, str(e))

        except Exception as e:
            bot.reply_to(message, e)
        
    else:
        bot.send_message(message.chat.id, "File " + message.document.file_name + " is not torrent file. MIME_TYPE: " + message.document.mime_type)

@bot.message_handler(commands=["vpnon","VpnOn"])
def open_vpn(message):
     os.system('systemctl start openvpn')
     bot.send_message(message.chat.id, "OpenVPN is starting.")

@bot.message_handler(commands=["vpnoff","VpnOff"])
def open_vpn(message):
     os.system('systemctl stop openvpn')
     bot.send_message(message.chat.id, "OpenVPN is stoping.")

@bot.message_handler(commands=["rtb","RTB"])
def restart_this_script(message):
    bot.send_message(message.chat.id, "Я ухожу в ребут. Сорри! :)")
    os.system('systemctl restart telegrambot.service')
#    quit()

#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#    print(flagStep)
#    bot.reply_to(message, message.text)

class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        length = int(cherrypy.request.headers['content-length'])
        json_string = cherrypy.request.body.read(length).decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook("https://bezmenovo.ddns.net/")
    cherrypy.config.update({
        'server.socket_host': '{{TELEGRAM_HOST}}',
        'server.socket_port': {{TELEGRAM_PORT}},
        'engine.autoreload.on': False
    })

    cherrypy.quickstart(WebhookServer(), '/', {'/': {}})
