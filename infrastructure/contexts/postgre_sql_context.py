from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuration_manager import ConfigurationManger
from constants import Constants
from resources.utils.rule_validation import ValidationError
from resources.utils.generals_utils import GeneralsUtils


class PostgreSqlContext:
    auto_dispose_bind = None
    SESSION_QUERY = "SET SESSION {} = {}"
    engine = None

    def configure(self, connection_string_name):
        connection_string_parts = ConfigurationManger.\
            get_connection_string(connection_string_name).split(',')

        if len(connection_string_parts) not in {2, 3}:
            raise Exception('Wrong number of connection parameters.')

        database_system, parameters = connection_string_parts[:2]
        configurations = ''

        if database_system not in Constants.DATABASE_SYSTEMS:
            raise Exception('Not supported database backend.')

        connection_string_split =\
            f"{database_system}://{parameters}{configurations}"

        self.__connection_string = connection_string_split
        self.__configurations = {}

        self.engine = create_engine(
            self.__connection_string,
            echo=False,
        )
        session = sessionmaker(bind=self.engine)
        session = session()

        return session
