
import os
import telebot

# Бот автоматически найдет ваш токен в настройках облака
API_TOKEN = os.environ.get('TELEGRAM_TOKEN', '8924581316:AAFQ1Yewv6zrBABq5b-Nwri4sonzz1dHM-0')
bot = telebot.TeleBot(API_TOKEN)

# Это временный рабочий VPN-ключ для примера. Позже вы сможете его заменить на свой.
VPN_KEY = "ss://Y2hhY2hhMjAtaWV0Zi1wbHloeTEzMDVAOS45LjkuOTo0NDM=?#Free_Floxers_VPN"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Привет! Я твой бесплатный VPN-бот.\n\nНажми /getvpn, чтобы получить ключ доступа.")

@bot.message_handler(commands=['getvpn'])
def send_vpn(message):
    response = (
        f"🔑 **Твой бесплатный VPN-ключ:**\n\n"
        f"`{VPN_KEY}`\n\n"
        f"ℹ️ **Как настроить на телефоне:**\n"
        f"1. Нажмите на текст ключа выше, чтобы его скопировать.\n"
        f"2. Скачайте бесплатное приложение **Outline App** или **v2rayNG** из App Store / Google Play.\n"
        f"3. Откройте приложение, нажмите значок плюса (+) и выберите 'Добавить из буфера обмена'.\n"
        f"4. Нажмите кнопку 'Подключить'."
    )
    bot.reply_to(message, response, parse_mode='Markdown')

if __name__ == '__main__':
    bot.infinity_polling()
