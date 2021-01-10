from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '14918ceccc0ed337cfaf3d7f2b9b4a944553199e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:adminrootpassword@127.0.0.1/eggCrack'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager(app)
login_manager.login_view = 'home'
login_manager.login_message_category = 'info'
bcrypt = Bcrypt(app)

from package import routes
