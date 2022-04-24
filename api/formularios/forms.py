from wtforms import Form
from wtforms import StringField, TextField,DateTimeField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from wtforms import validators
from wtforms import HiddenField
from wtforms import PasswordField
from datetime import datetime, timedelta
import email_validator
 
from wtforms import StringField, TextField, IntegerField, FloatField, SelectField ,DateField,TextAreaField, widgets, BooleanField

def lenght_honeypot(form, field):
    if len(field.data)>0:
        raise validators.ValidationError(' El campo debe estar vacio')

class indexForm(Form):
    honeypot=HiddenField('',[lenght_honeypot])
    origen=SelectField("origen",choices=[])
    clientes=SelectField("clientes",choices=[])
    tipo=SelectField("tipo",choices=[('flujo', 'flujo'), ('stock', 'stock')])
    fechadesde=TextField("fechadesde",validators=[validators.DataRequired()])
    fechahasta=TextField("fechadasta",validators=[validators.DataRequired()])
    dni=TextField("dni")
    primer_nombre=TextField("primer_nombre")
    segundo_nombre=TextField("segundo_nombre")
    apellido=TextField("apellido")
    testigo=BooleanField("testigo")
    demandado=BooleanField("demandado")
    abogado=BooleanField("abogado")
    autorizado=BooleanField("autorizado")
    actor=BooleanField("actor")
    
class loginForm(Form):
   

    email=StringField('username', render_kw={"placeholder": "pedro@legalhub.la"})
    password=PasswordField("Password",render_kw={"placeholder": "Ingrese su contraseña"})
    honeypot=HiddenField('',[lenght_honeypot])
    
       
class filterForm(Form):

    honeypot=HiddenField('',[lenght_honeypot])
    origen=SelectField("origen",choices=[])
    clientes=SelectField("clientes",choices=[])
    tipo=SelectField("tipo",choices=[])
    #fechadesde=TextField("fechadesde")
    #fechahasta=TextField("fechadasta")
    fechadesde=DateField("fechadesde",format="%Y-%m-%d",default=datetime.today)
    fechahasta=DateField("fechadasta",format="%Y-%m-%d",default=datetime.today)
    dni=TextField("dni")
    primer_nombre=TextField("primer_nombre")
    segundo_nombre=TextField("segundo_nombre")
    apellido=TextField("apellido")
    testigo=BooleanField("testigo")
    demandado=BooleanField("demandado")
    abogado=BooleanField("abogado")
    autorizado=BooleanField("autorizado")
    actor=BooleanField("actor")
    rol=SelectField("origen",choices=[('todos','Todos'),('testigo','Testigo'),('abogado','Abogado'),('actor','Actor'),('demandado','Demandado'),('autorizado','Autorizado')])
    muestra_cruce=BooleanField("muestra_cruce")
    lote=TextField("lote")
     

