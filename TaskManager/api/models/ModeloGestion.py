from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#crear instancia de la base para crear tablas
Base=declarative_base()

#Listado modelos de la Aplicacion

#USUARIO
class Usuario(Base):
    _tablename_='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(20))
    correo=Column(String(20))
    contraseña=Column(String(10))
    fechaRegistro=Column(Date)

#TASK
class Tareas(Base):
    _tablename_='Tareas'
    id=Column(Integer, primary_key=True, autoincrement=True)
    titulo=Column(Integer)
    descripcion=Column(String(100))
    fecha=Column(Date)
    Usuario=Column(String(50))
