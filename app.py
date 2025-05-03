from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        print(f"名前: {name}, メール: {email}, メッセージ: {message}")
        return render_template("contact.html", message="お問い合わせありがとうございました！")
    return render_template("contact.html", message=None)

if __name__ == "__main__":
    app.run(debug=True)

   