import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class UsersRolesRelation():
    __tablename__ = "users_roles_relation"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    role_id = Column(Integer, ForeignKey('Roles.id'))

    user = relationship("User")
    roles = relationship("Roles")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(120), unique=True, nullable=False)
    position = Column(String(100))
    slack_id = Column(Integer, unique=True)

    user = relationship("UsersRolesRelation")

    def __repr__(self):
        return '<User {}>'.format(self.full_name, self.position)


class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    role_name = Column(String(100), nullable=False)


class Bonus(Base):
    __tablename__ = "type_bonus"
    id = Column(Integer, primary_key=True)
    type = Column(String(20), nullable=False)
    description = Column(Text)

    def __repr__(self):
        return '<Bonus {}>'.format(self.type, self.description)


class Request(Base):
    __tablename__ = "request"
    id = Column(Integer, primary_key=True)
    creator = Column(Integer, ForeignKey('users.id'))
    status = Column(String(100), nullable=False)
    reviewer = Column(Integer, ForeignKey('users.id'))
    type_bonus = Column(Integer, ForeignKey('type_bonus.id'))
    date_of_creation = Column(DateTime(timezone=True), server_default=sqlalchemy.sql.func.now())
    last_changed_date = Column(Date)
    payment_date = Column(Date)

    creator_user = relationship("User")
    user_reviewer = relationship("User")
    bonus_type = relationship("Bonus")

    def __repr__(self):
        return '<Request {}>'.format(self.creator, self.status, self.payment_date)


