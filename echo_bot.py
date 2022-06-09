from flask import Flask, jsonify, request
from pyngrok import ngrok
import telebot
from waitress import serve
import os


app = Flask(__name__)

token = os.getenv('TOKEN')
telegram_url = f'https://api.telegram.org/bot{token}/setWebhook'
bot = telebot.TeleBot(token)

public_url = ngrok.connect(5000, bind_tls=True).public_url
bot.set_webhook(url=public_url)


@bot.message_handler()
def start_command(message):
    bot.send_message(message.chat.id, message.text)


@app.route("/", methods=["POST"])
def receive_update():
    try:
        bot.process_new_updates([telebot.types.Update.de_json(request.json)])
        return jsonify()
    except Exception:
        response = jsonify()
        response.status_code = 403
        return response


if __name__ == '__main__':
    serve(app, port=5000)
