# app.py file

from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_envvar('Name_of_env_var')

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=True)
    last_name = db.Column(db.String(100), nullable=True)

    created = db.Column(db.Datetime, nullable=True, default=datetime.now)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

#mysql details for connetion
db_link =  "mysql+pymysql://{}:{}@localhost/{}".format('root','Atp.db@jnj123','atp_db_new')
DB_EXTRACTION_URI = db_link
SQLALCHEMY_DATABASE_URI = db_link
SQLALCHEMY_TRACK_MODIFICATIONS = False

drop database if exists atp_db_new;
create database atp_db_new CHARACTER SET utf8 COLLATE utf8_general_ci;
grant all on atp_db_new.* to 'atpadmin'@'localhost' identified by 'atpAdmin@123'; 

#MONGO
#Mongo connection string
MONGO_CONNECT_STRING = 'mongodb://localhost:27017/'
MONGO_COLLECTION_NAME = 'prediction_db'

use prediction_db;
db.createUser( { user: "atpadmin", pwd: "Atp.db@jnj123", roles: [{role: "dbOwner", db: "prediction_db"}]});
// Test it using following command
db.auth("atpadmin", "Atp.db@jnj123")





