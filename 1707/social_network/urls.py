from .settings import project
import login_app
import chat_app

login_app.login.add_url_rule(
    '/', 
    view_func=login_app.render_login,
    methods = ["GET", "POST"],
)

login_app.login.add_url_rule(
    '/register', 
    view_func=login_app.render_register,
    methods=["GET", "POST"],
)

chat_app.chat.add_url_rule(
    '/chat', 
    view_func=chat_app.render_chat,
    methods=["GET", "POST"],
)

project.register_blueprint(blueprint=login_app.login)
project.register_blueprint(blueprint=chat_app.chat)