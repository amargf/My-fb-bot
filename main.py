from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "البوت يعمل بنجاح!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

if __name__ == "__main__":
    print("جاري تشغيل البوت...")
    keep_alive()
    # هنا سنضع كود التفاعل مع فيسبوك لاحقاً
    while True:
        time.sleep(10)
