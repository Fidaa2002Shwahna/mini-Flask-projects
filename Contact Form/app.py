from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail settings
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "programmerfidaa@gmail.com"
app.config["MAIL_PASSWORD"] = "your password >>> from gmail app password"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

mail = Mail()
mail.init_app(app)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        name =request.form.get("name", False)
        email =request.form.get("email", False)
        phone =request.form.get("phone", False)
        message =request.form.get("message", False)

        msg = Message('Hello', sender = email, recipients = ['programmerfidaa@gmail.com'])
        msg.body = message
        mail.send(msg)
        return render_template("index.html", success=True) 

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
