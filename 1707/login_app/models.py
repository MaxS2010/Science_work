from social_network.settings import DATABASE, login_manager


class User(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    login = DATABASE.Column(DATABASE.String)
    password = DATABASE.Column(DATABASE.String)
    is_active = DATABASE.Column(DATABASE.Boolean, default = True)    
    
    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))