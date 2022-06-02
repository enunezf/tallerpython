from sqlalchemy import Column, Integer, String

from .database import Base


class Recetas(Base):
    """
    Tabla para contener los encabezados de las recetas
    """
    __tablename__ = "recetas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    descripcion = Column(String)

