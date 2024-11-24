from flask import Flask, render_template, send_file
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/")
def index():
   return send_file('UniSign/website/DataSet/numbers/12/12_Twelve.mp4')

application = app

if __name__ == '__main__':
    app.run()
    