from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from flask_bootstrap import Bootstrap
from flask_migrate import Migrate





# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# initialize bootstrap
bootstrap = Bootstrap(app)
# initialize the database
db = SQLAlchemy(app)
# initialize the app with the extension
#db.init_app(app)
migrate = Migrate(app, db)




