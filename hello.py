from flask import Flask
app = Flask(__name__)

@app.route('/<int:date>')

def hellood(date):
    return "date=%d" %date
app.run()
