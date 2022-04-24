from flask import session
from flask import Flask, redirect, url_for
class validarSesion:
    def validarAdmin ():
        if  session:
            if session.__getitem__('admin') != 'S' or  session.__getitem__('admin') == 'None':
                return False;
            else:
                return True;
        else:
            return False;
    
    def validarCliente (): 

        if session :
            if session.__getitem__('admin') != 'N' or  session.__getitem__('admin') == 'None':
                return False;
            else:
                return True;
        else:
            return False;
   