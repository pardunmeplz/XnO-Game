from flask import redirect, url_for, request, jsonify,render_template, Blueprint
from gameLogic import Game

game_bp = Blueprint('game',__name__)
game = Game()

@game_bp.route("/game", methods =['GET','POST'])
def screen():
    if not game:
        return redirect(url_for("homePage"))
    
    if request.method == "POST":
        game.Play(request.json['index'])

    state = game.state()
    state['board'] = [i if x==0 else x.value for i,x in enumerate(state['board'])]
    state['player'] = state['player'].value

    if request.method == "GET":
        return render_template("game.jinja",message = "Play Game!", board = state["board"], player = state["player"])
    
    return jsonify(state) , 200