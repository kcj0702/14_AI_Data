from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
<<<<<<< HEAD
    return render_template()
=======
    return render_template("index.html")
>>>>>>> 44b0bac56b51f7a6bb4e7398147a37f14efd60d1


@app.route("/hello")
def hello():
    return "만나서 반갑습니다 응애"


@app.route("/user/<userId>")
def profile(userId):
    return f"{userId}\' profile"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run()
=======
    app.run(debug=True)
>>>>>>> 44b0bac56b51f7a6bb4e7398147a37f14efd60d1
