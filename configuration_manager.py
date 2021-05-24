# encoding: utf-8
import os

from pyms.constants import CONFIGMAP_FILE_ENVIRONMENT

from resources.utils.generals_utils import GeneralsUtils


class ConfigurationManger():

    CONFIG_CONNECTIONS_STRINGS_KEY = "CONNECTIONS_STRINGS"

    @staticmethod
    def get_connection_string(connection_string_name):
        if connection_string_name in os.environ:
            return os.environ[connection_string_name]

        connection_string =\
            GeneralsUtils.get_global_data(connection_string_name)

        if connection_string is None:
            connections_strings = ConfigurationManger.\
               get_config(ConfigurationManger.CONFIG_CONNECTIONS_STRINGS_KEY)

        return connections_strings.get(connection_string_name)

    @staticmethod
    def get_config(key, group=None):
        if key in os.environ:
            return os.environ[key]

        configurations = GeneralsUtils.read_file(
            os.environ.get(CONFIGMAP_FILE_ENVIRONMENT, 'config.yml'), 'yaml')

        configs = configurations["pyms"]["config"]
        if group:
            if GeneralsUtils.validate_attribute(group, configs):
                configs = configs[group]

            else:
                raise Exception("The requested configuration does not exist")

        if not GeneralsUtils.validate_attribute(key, configs):
            raise Exception("The requested configuration does not exist")

        return configs[key]
