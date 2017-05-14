from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from sqlalchemy import create_engine
engine = create_engine('sqlite:///diplomado.sqlite', echo=True)

"""
Creamos la session
"""
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombres = Column(String(140))
    apellidos = Column(String(140))
    usuario = Column(String(70))
    clave = Column(String(128))

    def __repr__(self):
        return "%s %s" %(self.nombres, self.apellidos)

Base.metadata.create_all(engine)


usuario = Usuario(nombres="Jonathan Dayessi",
                  apellidos="Sanchez Reyes",
                  usuario="dayessi",
                  clave="12345")

session.add(usuario)
session.commit()


print(session.query(Usuario).all())






