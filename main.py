from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Secret Key"

@app.route("/", methods=["GET", "POST"])
def main():
    if "turn" not in session:
        session["turn"] = "X"
        session["board"] = ["" for _ in range(9)]

    if request.method == "POST":
        cell = int(request.form["cell"])

        if not session["board"][cell]:
            session["board"][cell] = session["turn"]
            session["turn"] = "X" if session["turn"] == "O" else "O"

            return redirect("/")

    return render_template("index.html", turn=session["turn"], board=session["board"])


if __name__ == "__main__":
    app.run(debug=True)