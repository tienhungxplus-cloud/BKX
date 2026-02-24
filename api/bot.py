import telebot
from flask import Flask, request

# 1. Thay Token của bạn vào đây
TOKEN = "8679735939:AAHBVr6xcG..." 
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Chào bạn! Bot đã chạy trên Vercel (kho BKX) thành công.")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    # 2. Thay 'bkx.vercel.app' bằng link dự án Vercel mới của bạn nếu cần
    bot.set_webhook(url='https://bkx.vercel.app/' + TOKEN)
    return "Bot đang chạy...", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
