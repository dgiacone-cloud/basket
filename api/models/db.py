from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+pymysql://damiang:kD1\?D%2yk=@@34.78.101.148:3306/insurance_airflow')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
 