# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/About_me")
def About_me():
    About_me_data = [{
        'Name':'Nguyen Anh Quang',
        'Age':'23',
        'Location':'Hanoi',
        'Relationship_Status':'Single'
    }]
    return render_template ('About_me.html', data = About_me_data)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
