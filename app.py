from flask import Flask, render_template
from datetime import datetime

#__render_tamplates__ função do flask para renderizar tamplates


app = Flask(__name__)

#Criando lista [] - com Dicionário{}!
posts = [
    {
        "title": "First Post",
        "body": "Here is the First Post",
        "autor": "Jah",
        "created": datetime(2022,7,25)
    },

    {
        "title": "Second Post",
        "body": "Here is the second Post",
        "autor": "Jaxn",
        "created": datetime(2022,7,26)
    },
]
@app.route('/')
def index():
    return render_template("index.html", posts=posts)