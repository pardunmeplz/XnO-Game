from flask import Flask, render_template, redirect, url_for, request
from gameLogic import Game,Player,Response

app = Flask(__name__)
game = None
name = None

@app.route("/",methods = ["GET", "POST"])
def homePage():
    global game, name

    
    if request.method == "POST":
        game = Game()
        name = request.form["nm"]
        return redirect(url_for("gamePage"))

    return render_template("home.html") 
    
    
@app.route("/game")
def gamePage():
    if not game:
        return redirect(url_for("homePage"))

    board, player, gameOver, winningLine = game.state().values()

    draw = {Player.X:'X',Player.O:'O',0:''}
    board = [draw[x] for x in board]
    player = draw[player]
    
    return render_template("game.html",message = "Play Game!", board = board, player = player)





if __name__ == "__main__":
    app.run(debug = True)

