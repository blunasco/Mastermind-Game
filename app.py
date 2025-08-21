from flask import Flask, render_template
from routes import new_game_bp, guess_bp, end_game_bp
from models import db #import db from models package
from werkzeug.exceptions import HTTPException
from flask_migrate import Migrate

migrate = Migrate()  

def create_app():
    
    app = Flask(__name__) #createes flask application object
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mastermind.db" #points to the db
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.secret_key = "super-secret-key" 

    db.init_app(app) #connects the db created in models package to this flask app object
    migrate.init_app(app, db) #allows migrations (changes to the db) to this flask app object

    #registers bp, makes routes available to the app
    app.register_blueprint(new_game_bp)
    app.register_blueprint(guess_bp)
    app.register_blueprint(end_game_bp)

    #auto creates tables when app is first ran
    with app.app_context():  
        db.create_all()
        # log all errors

    @app.errorhandler(HTTPException)
    def handle_exception(e):  # noqa: F401
     return jsonify(error=str(e), description=e.description), e.code

    # Home route (renders frontend)
    @app.route("/")
    def home():
        return render_template("index.html")

    return app


if __name__== "__main__":
    app = create_app()
    app.run(debug=True)



