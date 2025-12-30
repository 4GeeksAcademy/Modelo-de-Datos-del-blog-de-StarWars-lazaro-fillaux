from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean,Table,Column,ForeignKey,Date
from sqlalchemy.orm import Mapped, mapped_column , relationship
from datetime import date
db = SQLAlchemy()
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable = False)
    password: Mapped[str] = mapped_column(nullable = False)
    profile: Mapped["Profile"] = relationship(back_populates="user")
    personajes:Mapped[List["Personaje"]] = relationship(secondary="favoritos", back_populates="users")

class Profile(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    edad: Mapped[int] = mapped_column(nullable = True)
    Fecha_de_subscripción: Mapped[date] = mapped_column(Date, default=date.today)
    user: Mapped["User"] = relationship(back_populates="profile")

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable = False)
    profile: Mapped["Profile_Planet"] = relationship(back_populates="planet")

class Profile_Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("planet.id"))
    edad: Mapped[int] = mapped_column(nullable = True)
    Tamaño: Mapped[int] = mapped_column(nullable = True)
    Distancia: Mapped[int] = mapped_column(nullable = True)
    user: Mapped["Planet"] = relationship(back_populates="profile_planet")

class Personaje(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable = False)
    profile: Mapped["Profile_Personaje"] = relationship(back_populates="personaje")
    users:Mapped[List["User"]] = relationship(secondary="favoritos", back_populates="personajes")

class Profile_Personaje(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("personaje.id"))
    edad: Mapped[int] = mapped_column(nullable = True)
    color_pelo : Mapped[str] = mapped_column(nullable = False)
    Sexo: Mapped[str] = mapped_column(nullable = False)
    user: Mapped["Personaje"] = relationship(back_populates="profile_personaje")


    
favoritos = Table(
    "favortitos",
    db.metadata,
    Column("personaje_id", ForeignKey("personaje.id")),
    Column("user_id", ForeignKey("user.id"))
)