from flask import render_template, request, redirect
from flask_login import current_user
from social_network.settings import socketio, emit, PATH_CHAT_DATA
import json


def save_data(data: list | dict):
    with open(PATH_CHAT_DATA, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def read_data():
    try:
        with open(PATH_CHAT_DATA, 'r') as f:
            data = json.load(f)
        return data
    except:
        save_data([])

def render_chat():
    try:
        if current_user.login:
            chat_data = read_data()          
            return render_template("chat.html", username = current_user.login, chat_data = chat_data)
        else:
            return redirect('/')
    except:
        return redirect('/')


@socketio.on("message")
def handle_message(message):
    new_message = {
        "text":message,
        "user":current_user.login
    }
    chat_data = read_data()
    chat_data.append(new_message)
    save_data(chat_data)
    emit('message', new_message, broadcast=True)