# coding=utf-8

import sys
import os
from flask import Flask

abspath = os.path.abspath(__file__)
app_root = os.path.dirname(abspath)
path = os.path.join(app_root, 'virtualenv.bundle')
sys.path.insert(0, path)
sys.path.insert(0, app_root)

app = Flask(__name__)
app.config.from_object('config')
from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
