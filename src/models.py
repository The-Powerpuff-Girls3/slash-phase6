from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
from database import Base

'''Creating a database model for users. '''
''' The __tablename__ attribute is used to define the name of the table in the database. '''

'''
    The user table has the following columns:
    Columns
    ----------
    id: int
        the id of the user
    email:str
        the email of the user
    username:str
        the username of the user
    first_name:str
        the first name of the user
    last_name:str
        the last name of the user
    hashed_password:str
        the hashed password of the user
'''


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    # list = relationship('Products', back_populates='users')


'''
    The user table has the following columns:
    Columns
    ----------
    product_id: int
        the id of the product
    user_id: int
        the id of the user
    product:str
        the product of the user
'''


class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    product = Column(String)
    # user = relationship('Users', back_populates='products')
