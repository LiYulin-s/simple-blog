import os
import sqlite3
import uuid

import markdown
from flask import Flask, abort, make_response, render_template

db = sqlite3.connect("simple-blog.db", check_same_thread=False)
cur = db.cursor()

app = Flask(__name__,
            static_folder="./themes",
            template_folder="./themes/templates")


@app.route('/')
def index():
    article_list = os.listdir("data\\articles\\")
    return render_template("index.html",
                           title="simple-blog",
                           head="My Blog",
                           text=markdown.Markdown)


@app.route('/file/<name>')
def getFile(name):
    sql = 'SELECT * FROM file WHERE name = ?'
    cur.execute(sql, [name])
    callList = cur.fetchall()
    if callList:
        response = make_response(callList[0][2])
        response.headers['Content-Type'] = 'image'
        return response
    else:
        abort(404)


if __name__ == "__main__":
    app.run()
