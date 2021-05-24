from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, mapper, sessionmaker
from sqlalchemy import create_engine, Table, MetaData
from infrastructure.contexts.postgre_sql_context import PostgreSqlContext

class BaseRepository():

    def __init__(self):

        self.context = PostgreSqlContext.configure("POSTGRESQL_DB_SET_AS")
        self.engine = create_engine(self.context.get_connection_string())
        self.meta = MetaData(bind=self.engine, schema="MS")

        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        
    def save_entity(self, entity):
        
        self.session.add(entity)

    def query_entity(self, entity):
        
        return self.session.query(entity)

    def commit_operation(self):
        
        self.session.commit()
        self.session.close()
        self.session.bind.dispose()

        
class MasterData(object): pass

class ServicePointVariable(object): pass

class RelationDevice(object):pass

class RelationDeviceDisable(object):pass