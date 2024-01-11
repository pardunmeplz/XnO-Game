from flask import Flask
from routes.gameRoute import game_bp
from routes.homeRoute import home_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(game_bp)

if __name__ == "__main__":
    app.run(debug = True)

