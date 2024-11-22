from flask import Flask, render_template, request
from sqlalchemy import func
from dotenv import load_dotenv
from db import db, init_db
from controllers.init_values import insert_initial_values
from controllers.dog_controller import dog_bp 
from controllers.nursery_controller import nursery_bp 
from controllers.caretaker_controller import caretaker_bp
from controllers.user_controller import user_bp
from models.user import User
from flask_login import LoginManager
import os

load_dotenv()

app = Flask(__name__, template_folder='views')

secret_key = os.urandom(24)
login_manager = LoginManager(app)

@app.route('/')
def index():
    welcome_message = request.args.get('welcome_message')
    print('index welcome_message: ' + str(welcome_message))
    return render_template('index.html', welcome_message=welcome_message)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

print(secret_key)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key

db.init_app(app)
init_db(app)
insert_initial_values(app)

# Importa y registra los blueprints de los controladores
app.register_blueprint(dog_bp, url_prefix='/dogs')
app.register_blueprint(nursery_bp, url_prefix='/nurseries')
app.register_blueprint(caretaker_bp, url_prefix='/caretakers')
app.register_blueprint(user_bp)  # Registrar en la raíz

if __name__ == '__main__':
    app.run(debug=True)
