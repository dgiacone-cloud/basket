from flask import render_template, request, redirect, url_for
from datetime import datetime
from api.formularios.forms import loginForm
from flask import Blueprint
from api.models.usuarios import Usuarios
from flask import session

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/', methods=['GET', 'POST'])
def getall():
    return render_template('inicio.html' )