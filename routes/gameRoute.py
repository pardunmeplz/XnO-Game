from flask import redirect, url_for, request, jsonify,render_template, Blueprint
from gameLogic import Game

game_bp = Blueprint('game',__name__)
game = Game()

@game_bp.route("/game", methods =['GET','POST'])
def screen():
    if not game:
        return redirect(url_for("homePage"))
    
    response = None
    if request.method == "POST":
        response = game.Play(request.json['index'])


    state = game.state()
    state['board'] = [i if x==0 else x.value for i,x in enumerate(state['board'])]
    state['player'] = state['player'].value
    state['gameOver'] = 1 if state['gameOver'] else 0 # Jinja has trouble with False in python vs false in javascript

    if request.method == "GET":
        return render_template("game.jinja",message = "Play Game!", state = state)
    
    return jsonify(state) , 200