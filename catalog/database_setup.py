#config
import os

from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


##class
class User(Base):
    __tablename__ = 'user'

    # mapper
    id = Column(
      Integer, primary_key = True)

    name = Column(
      String(250), nullable = False)

    email = Column(
      String(250), nullable = False)

    picture = Column(
      String(250))


class Category(Base):

    #table
    __tablename__ = 'category'

    # mapper
    id = Column ( 
      Integer, primary_key = True)

    name = Column (
      String(80), nullable = False)

    slug = Column (
      String(80), nullable = False)

    user_id = Column(
      Integer, ForeignKey('user.id'))

    user = relationship(User)


class Item(Base):

    #table
    __tablename__ = 'item'

    # mapper
    id = Column (
      Integer, primary_key = True)

    name = Column (
      String(80), nullable = False)

    slug = Column (
      String(80), nullable = False)

    created_date = Column(
      DateTime, default=datetime.utcnow())

    description = Column (
      String(1000))

    category_id = Column(
      Integer, ForeignKey('category.id'))
    
    category = relationship(Category)

    user_id = Column(
      Integer, ForeignKey('user.id'))

    user = relationship(User)


    @property
    def serialize(self):
        # returns object data in easily serializable format
        return {
            'name' :self.name,
            'slug' : self.slug,
            'id' : self.id,
            'created_date': str(self.created_date),
            'description': self.description,
            'category_id': self.category_id,
            'user_id': self.user_id
        }

####insert at end of file#####
# engine = create_engine(
#   'sqlite:///catalog.db'
#   )
# engine = create_engine('postgresql://catalog:catalogpass@localhost/catalogdb')
engine = create_engine( 'postgresql://catalog:catalog82205196@localhost/catalog')


#which goes into the db and adds the classes 
#we will soon create as new tables in our database.
Base.metadata.create_all(engine)
