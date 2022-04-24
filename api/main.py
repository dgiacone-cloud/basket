from flask import Flask
from flask import render_template
from flask import request 
from flask_fontawesome import FontAwesome
from flask_wtf import CsrfProtect  
from flask import make_response
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import traceback

app = Flask(__name__)
fa = FontAwesome(app)
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://damiang:kD1\?D%2yk=@@34.78.101.148:3306/insurance_airflow"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://dev_user:enOrDeCrN6SHuZ99@34.78.101.148/demandas_fraude_prod"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)


from .recursos.login import login


# Genero el Token para los formularios
csrf=CsrfProtect()

#Traigo las rutas de la carpeta recursos
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
 
app.register_blueprint(login)


 
 



