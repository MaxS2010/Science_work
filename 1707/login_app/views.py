from flask import render_template, request, redirect
from .models import User, DATABASE
from flask_login import login_user

def render_login():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        if login and password:
            user = User.query.filter_by(login=login).first()
            if user:
                if password == user.password:
                    login_user(user)
                    return redirect('/chat')
    return render_template('login.html')

def render_register():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if login and password:
            if password == confirm_password:
                new_user= User(login=login, password=password)
                DATABASE.session.add(new_user)
                DATABASE.session.commit()
                return redirect('/')

    return render_template('register.html')
