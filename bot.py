import requests
import time

TOKEN = "حط_التوكن_تاعك_هنا"
CHAT_ID = "حط_id_تاعك_هنا"

def get_quran():
    url = "https://api.alquran.cloud/v1/ayah/random"
    r = requests.get(url).json()
    ayah = r['data']['text']
    surah = r['data']['surah']['name']
    return f"{ayah}\n\nسورة: {surah}"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

while True:
    msg = get_quran()
    send_message(msg)
    time.sleep(86400) # 24 ساعة
