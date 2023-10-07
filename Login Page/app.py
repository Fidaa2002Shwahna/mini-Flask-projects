from flask import (
    abort,
    Flask,
    g,
    session,
    redirect,
    url_for,
    render_template,
    request
)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='root', password='Root2023@#$'))
users.append(User(id=2, username='Root', password='Root2023@#$'))

app = Flask(__name__)
app.secret_key = 'MY_secret_key'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']]
        if user:
            g.user = user[0]

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = next((x for x in users if x.username == username and x.password == password), None)
        if user:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
