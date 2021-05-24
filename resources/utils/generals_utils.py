import base64
import json
import os
import calendar
from datetime import datetime

import yaml

from constants import Constants


class GeneralsUtils:
    global_data = {}

    @staticmethod
    def decode_data(data):
        return base64.b64decode(data).decode('utf-8')

    @staticmethod
    def delete_columns(dicts, *keys):
        [dictionary.pop(key, None) for key in keys for dictionary in dicts]
        return dicts

    @staticmethod
    def encode_data(data):
        return base64.b64encode(data.encode("ascii"))

    @staticmethod
    def format_response_data(data):
        result = []
        if GeneralsUtils.validate_string(data) or\
           isinstance(data, (dict, int, float)):
            data = [data]

        elif isinstance(data, object) and not isinstance(data, list):
            data = [data.__dict__]

        if not isinstance(data, list):
            raise Exception("The data to format could not be processed")

        for datum in data:
            if isinstance(datum, (dict, int, float, list, str)):
                result.append(datum)

            elif isinstance(data, object):
                result.append(datum.__dict__)

        return result

    @staticmethod
    def get_datetime():
        return datetime.today().isoformat()

    @staticmethod
    def get_global_data(key):
        return GeneralsUtils.global_data.get(key)

    @staticmethod
    def get_request_body(request):
        result = None

        if not GeneralsUtils.validate_attribute("json", request, dict):
            data = request.data
            if isinstance(data, bytes) or\
               isinstance(data, str):
                result = json.loads(data)
            elif isinstance(data, dict):
                result = json.loads(data)
            elif isinstance(request.form, dict):
                result = request.form

        return result

    @staticmethod
    def read_file(path, output_type="json"):
        read_file_output_types = Constants.READ_FILE_OUTPUT_TYPES

        if not GeneralsUtils.validate_string(path):
            raise Exception

        if not os.path.isfile(path):
            raise Exception

        if not GeneralsUtils.\
           validate_attribute(output_type, read_file_output_types, str):
            raise Exception

        with open(path, "r") as text_file:
            if output_type == "json":
                result = json.load(text_file)

            elif output_type == "yaml":
                result = yaml.safe_load(text_file)

        return result

    @staticmethod
    def set_global_data(key, value):
        if not GeneralsUtils.validate_string(key):
            raise Exception

        GeneralsUtils.global_data[key] = value

    @staticmethod
    def validate_attribute(attribute_name,
                           structure,
                           attribute_types_allowed=None):
        result = False

        if not GeneralsUtils.validate_string(attribute_name) or\
           not isinstance(structure, (dict, tuple, list)) or\
           attribute_name not in structure:
            return False

        if attribute_types_allowed is None:
            result = True

        elif isinstance(attribute_types_allowed, type) or\
                (
                    isinstance(attribute_types_allowed, tuple) and
                    all(isinstance(type_attribute_allowed, type)
                        for type_attribute_allowed in attribute_types_allowed)
                ):

            if isinstance(structure, dict):
                attribute = structure[attribute_name]
            else:
                attribute =\
                    next(item for item in structure if attribute_name == item)

            if isinstance(attribute, attribute_types_allowed):
                result = True

        else:
            return False

        return result

    @staticmethod
    def validate_string(value):
        if not isinstance(value, str):
            return False

        if str.strip(value) == "":
            return False

        return True

    @staticmethod
    def try_parse_date_time(value):
        DATE_TIME_FORMATS = (
            '%Y-%m-%dT%H:%M:%SZ',
            '%Y-%m-%dT%H:%M:%S.%fZ',
            '%Y-%m-%d %H:%M:%SZ',
            '%Y-%m-%d %H:%M:%S.%fZ',
            '%Y-%m-%dT%H:%M:%S',
            '%Y-%m-%dT%H:%M:%S.%f',
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d %H:%M:%S.%f',
            '%m//%d//%Y %H:%M',
            '%Y-%B'
        )
        for date_time_format in DATE_TIME_FORMATS:
            try:
                return datetime.strptime(value, date_time_format)

            except ValueError:
                pass

        raise ValueError('no valid date format found')

    @staticmethod
    def try_parse_int(value):
        try:
            return int(value)

        except ValueError:
            return None

    @staticmethod
    def try_parse_date_time_custom_format(value, time_format):
        """This method is used for try parse datetime to custom format
        Args:
            time_format (string): Time format to parse
            value (string): Value to format
        Returns:
            A datetime format
        """
        try:
            return datetime.strptime(value, time_format)

        except ValueError:
            pass

    @staticmethod
    def get_date_yyyymmdd(date_str):
        date = GeneralsUtils().try_parse_date_time(date_str)
        return date.strftime('%Y%m%d')

    @staticmethod
    def get_date_yyyymm(date_str):
        date = GeneralsUtils().try_parse_date_time(date_str)
        return date.strftime('%Y%m')

    @staticmethod
    def get_start_and_end_date_in_custom_format(
        month_name,
        year,
        custom_format
    ):
        """Get the start and end date for month and year.

        Args:
            month_name (string): The month name (January, February, etc).
            year (number): The year

        Returns:
            array: Position zero is start date, and position one is end date.
        """
        if isinstance(year, str):
            year = int(year)
        month = datetime.strptime(month_name, "%B").month
        start = datetime(year, month, 1).strftime(custom_format)
        end = datetime(
            year,
            month,
            calendar.monthrange(year, month)[1]
        ).strftime(custom_format)
        return [start, end]

    @staticmethod
    def split_event_type(event_type):
        """This method is used for separate evenType

        Args:
            event_type string: eventType received by sqs

        Returns:
            array: eventType in array
        """
        result = []

        if not isinstance(event_type, str):
            return []

        result = event_type.split("-")

        if len(result) != 3:
            return []

        result.extend(result[2].split("."))
        result.remove(result[2])

        if len(result) != 4:
            return []

        return result
