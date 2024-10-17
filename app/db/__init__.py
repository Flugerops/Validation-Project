from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .helpers import Base


class AsyncDB:
    ENGINE = create_engine("sqlite:///books.db")
    SESSION = sessionmaker(bind=ENGINE)
    
    @classmethod
    def up(cls):
        Base.metadata.create_all(cls.ENGINE)
    
    @classmethod
    def down(cls):
        Base.metadata.drop_all(cls.ENGINE)
        
    @classmethod
    def migrate(cls):
        Base.metadata.drop_all(cls.ENGINE)
        Base.metadata.create_all(cls.ENGINE)
        
    # @classmethod         #For SQLModel Dependency Injection
    # def get_session(cls):
    #     try:
    #         yield cls.SESSION
    #     finally:
    #         cls.SESSION.commit()
    #         cls.SESSION.close()
            
from .models import Book