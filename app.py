from flask import Flask
from datetime import datetime
from zoneinfo import ZoneInfo  

app = Flask(__name__)

@app.route('/')
def hello():
    ist_time = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello from Dr. ViKi DevOps Pipeline!<br>Current Time: {ist_time}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
