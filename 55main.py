import requests
from chatterbot import ChatBot

TOKEN = '7120326643:AAG1Hrcthb1ot9fZjY5ub5GiTP40djBIIyk'

# إنشاء بوت الدردشة باستخدام ChatterBot
bot = ChatBot('MyBot')

def analyze_message(message):
    # تحليل الرسالة باستخدام بوت الدردشة
    response = bot.get_response(message)
    return str(response)

def handle_message(update):
    chat_id = update['message']['chat']['id']
    message_text = update['message']['text']
    
    # تحليل الرسالة والحصول على الرد المناسب
    response = analyze_message(message_text)
    
    # إرسال الرد إلى المستخدم
    send_message(chat_id, response)

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, json=payload)

def main():
    offset = None
    while True:
        url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
        if offset:
            url += f'?offset={offset}'
        response = requests.get(url)
        updates = response.json()['result']
        for update in updates:
            offset = update['update_id'] + 1
            if 'message' in update:
                handle_message(update)

if __name__ == '__main__':
    main()
