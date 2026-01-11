import facebook
import time
from flask import Flask
import threading

app = Flask(__name__)

# ضع الـ Token الخاص بك هنا (سأعلمك كيف تحصل عليه لاحقاً)
TOKEN = 'YOUR_FACEBOOK_ACCESS_TOKEN'

def fb_task():
    graph = facebook.GraphAPI(access_token=TOKEN)
    while True:
        try:
            # مثال: نشر منشور كل ساعة
            message = "أهلاً بكم! هذا منشور تلقائي لزيادة التفاعل 🚀"
            graph.put_object(parent_object='me', connection_name='feed', message=message)
            print("تم النشر على فيسبوك بنجاح!")
        except Exception as e:
            print(f"خطأ في فيسبوك: {e}")
        
        time.sleep(3600) # الانتظار لمدة ساعة

@app.route('/')
def home():
    return "البوت يعمل والاتصال بفيسبوك مفعل!"

if __name__ == "__main__":
    # تشغيل مهمة فيسبوك في خلفية السيرفر
    threading.Thread(target=fb_task).start()
    # تشغيل السيرفر للبقاء مستيقظاً
    app.run(host='0.0.0.0', port=8080)
