from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "Secret Key"

@app.route("/")
def main():
    turn = "X" #temporary var
    return render_template("index.html", turn=turn)


if __name__ == "__main__":
    app.run(debug=True)