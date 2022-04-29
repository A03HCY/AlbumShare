from flask import *
from io import BytesIO
import requests
import os

app = Flask(__name__)
app.secret_key = 'C-i7tyW8~gmckBS'


@app.route("/", methods=['GET'])
def home():
    ls = os.listdir('./templates/')
    la = []
    for i in ls:
        name = i[0:-5]
        la.append(name)
    return str(la)


@app.route("/<name>", methods=['GET'])
def reto(name=''):
    try:return render_template(name+'.html')
    except:return 'No'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)