from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "WebPage Here"

if __name__ == '__main__':
    app.run()