from .import  db
from sqlalchemy import Column, Integer, String, Float, ForeignKey , Numeric
from sqlalchemy.orm import sessionmaker, relationship

class OutNodos(db.Base):
        __tablename__ = 'out_nodos'
        key=Column(Integer, primary_key=True)
        target=Column(String(60))
        initials=Column(String(60))
        score=Column(Numeric(precision=10, scale=2, asdecimal=True))
        red=Column(Integer)
        expediente_weight=Column(Integer)
        node_weight=Column(Integer)
        red_score=Column(Numeric(precision=10, scale=2, asdecimal=True))
        hex=Column(String(60))
        aseguradora=Column(Integer)
        demandado=Column(Integer)
        actor=Column(Integer)
        testigo=Column(Integer)
        abogado=Column(Integer)
        medico=Column(Integer)
        freq_total=Column(Integer)
        mult_roles=Column(Integer)
        mult_abog=Column(Integer)

        def __init__(self,target,initials,score,red,expediente,node_weight,red_score,hex,aseguradora,demandado,actor,testigo,abogado, medico, freq_total, mult_roles,mult_abog):
                self.target=target
                self.initials=initials
                self.score=score
                self.red=red
                self.expediente=expediente
                self.node_weight=node_weight
                self.red_score=red_score
                self.hex=hex
                self.aseguradora=aseguradora
                self.demandado=demandado
                self.actor=actor
                self.testigo=testigo
                self.abogado=abogado
                self.medico=medico
                self.freq_total=freq_total
                self.mult_roles=mult_roles
                self.mult_abog=mult_abog 
        

        