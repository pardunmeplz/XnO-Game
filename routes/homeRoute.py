from flask import Blueprint, redirect, request, url_for, render_template
from gameLogic import Game

home_bp = Blueprint('home',__name__)

@home_bp.route("/",methods = ["GET", "POST"])
def screen():
    global game, name
    
    if request.method == "POST":
        game = Game()
        name = request.form["nm"]
        return redirect(url_for("game.screen"))

    return render_template("home.jinja") 