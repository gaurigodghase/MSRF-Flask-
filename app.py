print("hello")
'''from flask import (
    Flask,
    app,
    render_template

)'''

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Gauri', password='password1'))
users.append(User(id=2, username='Omkar', password='password2'))
users.append(User(id=3, username='Chitrakant', password='password3'))

print(users)



app = Flask(__name__)

@app.route('/login',methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == "__main__":
    app.run()



