from datetime import datetime
from jsonschema import validate, ValidationError

from project.infrastructure.repositories.common_repository import\
    CommonRepository
from project.resources.utils.generals_utils import GeneralsUtils
from project.services.domain_service import DomainService


class ValidationUtils():
    CONST_NAME_NODE_PROPERTIES = "properties"
    CONST_NAME_NODE_REQUIRED = "required"
    CONST_NAME_NODE_DOMAIN = "domain"
    CONST_NAME_NODE_PARAMETERS_DOMAIN = "parametersDomain"
    CONST_NAME_NODE_DEFAULT = "default"
    CONST_NAME_NODE_PARAMETERS_DEFAULT = "parametersDefault"
    CONST_NAME_PARAMETER = "attribute"
    CONST_IDENTIFY_FUNCTION = "f'"
    CONST_KEY_BRAND = "brand"
    CONST_KEY_MODEL = "model"
    CONST_KEY_CONNECTION_TYPE = "communicationCode"
    CONST_NAME_FUNCTION_PARAMETERS = "set_parameters"
    MSJ_VALIDATION_ERROR_DOMAIN = "Value is not found in defined domain"

    local_storage = {}

    def __init__(self):
        self.local_storage = {}

    def validate_attributes(
            self,
            dictionary,
            schema,
            set_default_value=True,
            entity_name=None):
        self.validation_initializer(dictionary, schema, entity_name)
        result_messages = []
        result_messages = list(
            map(lambda json_node:
                self.validate_node(json_node, set_default_value),
                self.schema[self.CONST_NAME_NODE_PROPERTIES]))
        return result_messages

    def validation_initializer(self, dictionary, schema, entity_name):
        self.dictionary = dictionary
        self.schema = schema
        self.caller_functions = CallerFunctions()

        if entity_name == "device":
            if self.CONST_KEY_BRAND in\
               self.dictionary and self.CONST_KEY_MODEL in self.dictionary:
                variable_brand = self.dictionary[self.CONST_KEY_BRAND]
                variable_model = self.dictionary[self.CONST_KEY_MODEL]
                variable_comunication_type =\
                    self.dictionary[self.CONST_KEY_CONNECTION_TYPE]\
                    if self.CONST_KEY_CONNECTION_TYPE in self.dictionary\
                    else ""

            else:
                variable_brand = ""
                variable_model = ""
                variable_comunication_type = ""

            function = getattr(
                self.caller_functions,
                self.CONST_NAME_FUNCTION_PARAMETERS)
            function(
                variable_brand,
                variable_model,
                variable_comunication_type)

    result = []

    def validate_node(self, json_property, set_default_value):
        is_required = True\
            if json_property in self.schema[self.CONST_NAME_NODE_REQUIRED]\
            else False

        json_schema_node =\
            self.schema[self.CONST_NAME_NODE_PROPERTIES][json_property]

        try:
            if json_property not in self.dictionary:
                self.dictionary[json_property] = None

            property_value = self.dictionary[json_property]

            if isinstance(property_value, str) and\
               not GeneralsUtils.validate_string(property_value):
                del self.dictionary[json_property]

            self.dictionary[json_property] =\
                self.get_default_value(json_property)\
                if set_default_value\
                else property_value or None

            if self.dictionary[json_property] is None and\
               property_value is False:
                self.dictionary[json_property] = False

            item = {
                "json_property": json_property,
                "value": self.dictionary[json_property]
            }

            self.result.append(item)

            validate(self.dictionary[json_property], json_schema_node)

            if self.CONST_NAME_NODE_DOMAIN in json_schema_node:
                if not self.execute_function(
                   json_property,
                   self.CONST_NAME_NODE_DOMAIN,
                   self.CONST_NAME_NODE_PARAMETERS_DOMAIN):
                    raise ValidationError(
                        self.MSJ_VALIDATION_ERROR_DOMAIN, json_property)

            return {
                "property": json_property,
                "resultValidation": "success",
                "isRequired": is_required
            }

        except ValidationError as error:
            message_error = str(error.message)
            self.dictionary[json_property] = None
            self.dictionary[json_property] =\
                self.get_default_value(json_property)
            item = message_error
            return {
                "property": json_property,
                "resultValidation": message_error,
                "isRequired": is_required
            }

        except Exception as error:
            raise error

    def get_default_value(self, json_property):
        json_schema_node =\
            self.schema[self.CONST_NAME_NODE_PROPERTIES][json_property]

        try:
            if json_property in self.dictionary and\
               self.dictionary[json_property] is not None:
                return self.dictionary[json_property]

            else:
                if self.CONST_NAME_NODE_DEFAULT in json_schema_node and\
                   (not isinstance(json_schema_node[
                    self.CONST_NAME_NODE_DEFAULT], str) or
                    self.CONST_IDENTIFY_FUNCTION not in json_schema_node[
                        self.CONST_NAME_NODE_DEFAULT]):
                    default_value =\
                        json_schema_node[self.CONST_NAME_NODE_DEFAULT]
                    self.dictionary[json_property] = default_value

                    return default_value

                elif self.CONST_NAME_NODE_DEFAULT in\
                        json_schema_node and self.CONST_IDENTIFY_FUNCTION in\
                        json_schema_node[self.CONST_NAME_NODE_DEFAULT]:
                    result_function =\
                        self.execute_function(
                            json_property,
                            self.CONST_NAME_NODE_DEFAULT,
                            self.CONST_NAME_NODE_PARAMETERS_DEFAULT)
                    self.dictionary[json_property] = result_function

                    return result_function

                else:
                    return None

        except Exception as error:
            raise error

    def execute_function(
            self,
            json_property,
            function_node_name,
            parameter_node_name):
        rules = self.schema[self.CONST_NAME_NODE_PROPERTIES][json_property]

        if function_node_name in rules:
            if isinstance(rules[function_node_name], str):
                function_name =\
                    rules[function_node_name].replace(
                        self.CONST_IDENTIFY_FUNCTION, "")
                function = getattr(self.caller_functions, function_name)
                parameters = {}

            if parameter_node_name in rules:
                parameters = dict(
                    map(lambda name_parameter: (
                        name_parameter,
                        self.dictionary[name_parameter])
                        if name_parameter in self.dictionary else
                        (name_parameter, None), rules[parameter_node_name]))

            if json_property in self.dictionary:
                parameters[self.CONST_NAME_PARAMETER] =\
                    self.dictionary[json_property]

            if function_node_name == "default":
                parameters[self.CONST_NAME_PARAMETER] = json_property

            return function(**parameters)
        else:
            return True

    def set_default_values(
        self,
        dictionary,
        schema,
        entity_name=None
    ):
        """This method set the values by defect in properties the dictionary.

        Args:
            dictionary (dict): Entity with values
            schema (dict): Schema to validate
            entity_name (string): Entity name
        """
        self.validation_initializer(dictionary, schema, entity_name)
        for key, value in dictionary.items():
            if value is None and\
               key in self.schema[self.CONST_NAME_NODE_PROPERTIES] and\
               'default' in self.schema[self.CONST_NAME_NODE_PROPERTIES][key]:
                self.dictionary[key] = self.schema[self.CONST_NAME_NODE_PROPERTIES][key]['default']


class CallerFunctions():

    def __init__(self):
        self.local_storage = {}

    def set_parameters(self, brand, model, communication_type):
        domain_service = DomainService()
        self.domains_data = {}
        if f"{brand}-{model}" in self.local_storage:
            self.domains_data = self.local_storage[f"{brand}-{model}"]

        else:
            self.domains_data = domain_service.get_brand_model(brand, model)
            self.local_storage[f"{brand}-{model}"] = self.domains_data

        self.default_data = []

        if len(self.domains_data) > 0:
            entity_name = "validationSchema"
            default_data_device = CommonRepository(entity_name=entity_name)
            local_storage_key = f"{2}_{entity_name}"
            if local_storage_key in self.local_storage:
                all_default_data = self.local_storage[local_storage_key]

            else:
                all_default_data = default_data_device.\
                    select_one(2, entity_name)[0]["jsonSettingMai"]
                self.local_storage[local_storage_key] = all_default_data

            list_default_data = list(
                filter(lambda x:
                       x["brand"] == brand and
                       x["model"] == model and
                       x["connectionType"] == communication_type,
                       all_default_data))

            if len(list_default_data) > 0:
                self.default_data = list_default_data[0]

    def filter_data(self, key_value, value):
        flag = False
        list_domains_data = list(
            filter(lambda x:
                   x[key_value] == value,
                   self.domains_data))

        if len(list_domains_data) > 0:
            flag = True

        return flag

    def default_values_by_communication_type(
            self,
            key_value,
            communication_type):
        default_value = None
        list_domains_data = list(
            filter(lambda x:
                   x["communicationCode"] == communication_type,
                   self.domains_data))

        if len(list_domains_data) > 0:
            default_value = list_domains_data[0][key_value]

        return default_value

    def domain_brand(self, attribute):
        return True if len(self.domains_data) > 0 else False

    def domain_model(self, attribute):
        return True if len(self.domains_data) > 0 else False

    def domain_pt(self, attribute):
        return True

    def domain_ct(self, attribute):
        return True

    def domain_communication_code(self, attribute):
        return self.filter_data("communicationCode", attribute)

    def default_value_assignment(self, attribute):
        return self.default_data[attribute]\
               if len(self.default_data) > 0 else 0
