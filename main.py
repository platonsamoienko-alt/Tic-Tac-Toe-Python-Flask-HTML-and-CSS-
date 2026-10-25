from flask import Flask, render_template, request, redirect, session
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

WIN_COMBS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@app.route("/", methods=["GET", "POST"])
def main():
    if "game_state" not in session:
        session["turn"] = "X"
        session["x_cells"] = []
        session["o_cells"] = []
        session["board"] = ["" for _ in range(9)]
        session["game_state"] = "Game is still on."

    if request.method == "POST":
        cell = int(request.form["cell"])

        if session["game_state"] == "Game is still on.":
            if not session["board"][cell]:
                session["board"][cell] = session["turn"]
                if session["turn"] == "X":
                    session["turn"] = "O"
                    session["x_cells"].append(cell)                    

                    for win_comb in WIN_COMBS:
                        if all(cell in session["x_cells"] for cell in win_comb):
                            session["game_state"] = "X won!"
                else:
                    session["turn"] = "X"
                    session["o_cells"].append(cell)

                    for win_comb in WIN_COMBS:
                        if all(cell in session["o_cells"] for cell in win_comb):
                            session["game_state"] = "O won!"

                if (
                    not "" in session["board"]
                        and
                    session["game_state"] == "Game is still on."
                ):
                    session["game_state"] = "Draw!"
                session.modified = True

            return redirect("/")

    return render_template("index.html", turn=session["turn"], board=session["board"], game_state = session["game_state"])

@app.route("/reset")
def reset():
    session["turn"] = "X"
    session["x_cells"] = []
    session["o_cells"] = []
    session["board"] = ["" for _ in range(9)]
    session["game_state"] = "Game is still on."

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)