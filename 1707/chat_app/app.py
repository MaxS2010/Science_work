import flask 

chat = flask.Blueprint(
    name = "chat",
    import_name = "chat_app",
    template_folder = "templates",
    static_folder = "static",
    static_url_path = "/chat/"
)