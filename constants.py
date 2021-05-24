class Constants:
    BOOLEAN = "boolean"

    BROKER_MESSAGE_SOURCE_VALUE = "MeteringSystem"

    CONFIG_APP_VERSION_KEY = "APP_VERSION"
    CONFIG_ENDPOINTS_ORCHESTRATOR_KEY = "ENDPOINTS_ORCHESTRATOR"
    CONFIG_ENDPOINTS_ORCHESTRATOR_TOPOLOGY_KEY =\
        "ORCHESTRATOR_TOPOLOGY_METERING"
    CONFIG_ENDPOINTS_ORCHESTRATOR_UDF_KEY = "ORCHESTRATOR_UDF"
    CONFIG_ENDPOINTS_ORCHESTRATOR_VARIABLE_TOPOLOGY_KEY =\
        "ORCHESTRATOR_VARIABLE_TOPOLOGY"
    CONFIG_ENDPOINTS_TOPOLOGY_CHARGER_KEY =\
        "VARIABLE_RELATIONSHIP"

    PROCESS_NAME_UDF_ASSOCIATE = 'associate'

    CONNECTION_STRING_POSTGRESQL_DB_PAP_RD_KEY = "POSTGRESQL_DB_PAP_RD"
    CONNECTION_STRING_POSTGRESQL_DB_PAP_MS_KEY = "POSTGRESQL_DB_PAP_MS"

    CONNECTION_NAME_KEY = 'connectionName'
    CONNECTION_EXTERNAL_NAME_KEY = 'externalSystemName'

    CONTENT_TYPE_KEY = "Content-Type"
    CONTENT_TYPE_VALUE = "application/json"

    COUNT_ROWS_BY_PAGE_TOPOLOGY_KEY = "COUNT_ROWS_BY_PAGE_TOPOLOGY"

    DATABASE_SYSTEMS = ('postgresql', 'redis', 'redshift', 'sqlite')
    DATABASE_DRIVERS = ('pg8000', 'psycopg2')
    DATABASE_WITH_AUDIT = ('postgres', 'postgresql')

    DATA_TYPE = "dataType"
    DATE = 'date'
    DATE_TIME = "datetime"
    DEFAULT = "default"
    DEFAULT_VALUE = "defaultValue"

    ELASTIC_CACHE_CLIENT_NAME = "elasticache"
    ENTITY = "entity"
    ENTITY_ID = "entityId"
    ENUM = "enum"
    ERROR = "Error"
    ERROR_REQUEST_ORCHESTRATOR =\
        "Error to send http request to Orchestrator MS"

    ENTITY_ATTRIBUTE_RESULT_KEY = "result"
    ENTITY_ATTRIBUTE_TO_INSERT_KEY = "toInsert"
    ENTITY_ATTRIBUTE_WARNING_RESULT_KEY = "warningResult"
    ENTITY_ATTRIBUTE_OWNER_KEY = "ownerData"
    ENTITY_ATTRIBUTE_USER_CREATE_KEY = "userCreate"
    ENTITY_ATTRIBUTE_USER_UPDATE_KEY = "userUpdate"

    CONFIGURATION_ENTITY_ATTRIBUTES = (
        ENTITY_ATTRIBUTE_RESULT_KEY,
        ENTITY_ATTRIBUTE_TO_INSERT_KEY,
        ENTITY_ATTRIBUTE_WARNING_RESULT_KEY,
        ENTITY_ATTRIBUTE_OWNER_KEY,
        ENTITY_ATTRIBUTE_USER_CREATE_KEY,
        ENTITY_ATTRIBUTE_USER_UPDATE_KEY
    )

    EXCLUDED_REQUEST_PATHS = ("swagger",)
    EXCLUDE_REQUEST_VERBS = ("OPTIONS",)

    GLOBAL_DATA_HES_KEY = "hes"
    GLOBAL_DATA_OWNER_KEY = "owner"
    GLOBAL_DATA_USER_ID_KEY = "user_id"
    GLOBAL_DATA_TRANSACTION_ID_KEY = "transaction_id"
    GLOBAL_DATA_IP_KEY = "source_ip"

    GLOBAL_SESSION_TRANSACTION_ID_KEY = "globalSession.transaction_id"
    GLOBAL_SESSION_USER_ID_KEY = "globalSession.user_id"
    GLOBAL_SESSION_OWNER_ID_KEY = "globalSession.owner_id"
    GLOBAL_SESSION_SOURCE_ID_KEY = "globalSession.source_id"
    GLOBAL_SESSION_SOURCE_IP_KEY = "globalSession.source_Ip"

    BROKER_MESSAGE_PROCESS_VALUE = "brokerMessage"

    BODY_NODE_OWNER_KEY = "owner"
    BODY_NODE_SERVICE_POINTS_KEY = "servicePoint"
    BODY_NODE_DEVICES_KEY = "device"
    BODY_NODE_TYPE = "typePowerSupply"
    BODY_NODE_EVENT_DATE = "eventDate"
    BODY_NODE_NAME = "name"
    BODY_NODE_MODULE = "module"
    BODY_NODE_STATE = "deviceState"
    BODY_NODE_REASON = "reason"
    BODY_NODE_NAME_POS = "namePos"
    BODY_NODE_DEVICE_ID_KEY = "deviceId"
    BODY_NODE_DEVICE_MAP_ID_KEY = "idDev"
    BODY_NODE_RELATIONS_DEVICE_KEY = "relationDevice"
    BODY_NODE_METERING_SYSTEM = "meteringSystem"
    BODY_NODE_SERVICE_POINTS_VARIABLES_KEY = "servicePointVariable"
    BODY_NODE_OWNER_OWNER_KEY = "owner"
    BODY_NODE_OWNER_GUID_FILE_KEY = "guidFile"
    BODY_NODE_OWNER_HES_KEY = "hes"
    BODY_NODE_VARIABLES_KEY = "variable"
    BODY_NODE_EXCEPTION_MISSING_PARAMETER = "missing parameters"
    BODY_PACKAGE_OWNER_PARAMETERS = (
        {
            "NAME": BODY_NODE_OWNER_OWNER_KEY,
            "GLOBAL_DATA_KEY": GLOBAL_DATA_OWNER_KEY,
            "REQUIRED": True
        },
        {
            "NAME": BODY_NODE_OWNER_GUID_FILE_KEY,
            "GLOBAL_DATA_KEY": GLOBAL_DATA_TRANSACTION_ID_KEY,
            "REQUIRED": True
        },
        {
            "NAME": BODY_NODE_OWNER_HES_KEY,
            "GLOBAL_DATA_KEY": GLOBAL_DATA_HES_KEY,
            "REQUIRED": True
        }
    )

    DEFAULT_VALUES = {
        "device": {
            "map_information_id": 1,
            "order": 1
        },
        "service_point_variable": {
            "log_number": 1
        }
    }

    DOMAIN_NAME_CLASS_DEVICE_CATEGORY = "DEV_CATEGO"
    DOMAIN_NAME_CLASS_DEVICE_METERING_TYPE = "DEV_METYPE"
    DOMAIN_NAME_CLASS_DEVICE_TYPE = "DEV_TYPES"
    DOMAIN_NAME_CLASS_DEVICE_STATUS = "TRA_STATUS"
    DOMAIN_NAME_CLASS_POWER_SUPPLY_STATUS = "POWSUPSTAT"
    DOMAIN_NAME_CLASS_POWER_SUPPLY_TYPE = "POWSUPTYPE"
    DOMAIN_NAME_CLASS_VARIABLE_TYPE = "VDI_TYPVAR"
    DOMAIN_NAME_CLASS_STANDARD_VARIABLE = "STANDARVAR"
    DOMAIN_NAME_CLASS_SCHENTEPAP = "SCHENTEPAP"

    DOMAIN_VALUE_DEVICE_TYPE_ELECTRICAL_METER = "ELECTRICAL METER"

    GRIDS = ("meteringSystem", "readingTypeCode",
             "task_service_points", "task_variables")

    ID = "id"
    IS_REQUIRED = "isRequired"

    LIST_VALUES = "listValues"
    LOG_BUSINESS_ACTION_SET_UP = "SetUp"
    LOG_BUSINESS_ACTION_CREATE = "Create"
    LOG_BUSINESS_ACTION_UPDATE = "Update"
    LOG_BUSINESS_ACTIONS = {
        "SET_UP": LOG_BUSINESS_ACTION_SET_UP,
        "CREATE": LOG_BUSINESS_ACTION_CREATE,
        "UPDATE": LOG_BUSINESS_ACTION_UPDATE
    }
    LOG_BUSINESS_CATEGORY_DEBUG = "Debug"
    LOG_BUSINESS_CATEGORY_ERROR = "Error"
    LOG_BUSINESS_CATEGORY_INFORMATION = "Information"
    LOG_BUSINESS_CATEGORY_VALUE = "Topology"
    LOG_BUSINESS_CATEGORY_WARNING = "Warning"
    LOG_BUSINESS_CATEGORIES = {
        "DEBUG": LOG_BUSINESS_CATEGORY_DEBUG,
        "ERROR": LOG_BUSINESS_CATEGORY_ERROR,
        "INFORMATION": LOG_BUSINESS_CATEGORY_INFORMATION,
        "WARNING": LOG_BUSINESS_CATEGORY_WARNING
    }
    LOG_BUSINESS_PROCESS_VALUE = "logtopology"
    LOG_BUSINESS_RESULT_FAILED = "Failed"
    LOG_BUSINESS_RESULT_SUCCESSFUL = "Successful"
    LOG_BUSINESS_RESULT_UNKNOWN = "Unknown"
    LOG_BUSINESS_RESULT_WARNING = "Warning"
    LOG_BUSINESS_RESULTS = {
        "FAILED": LOG_BUSINESS_RESULT_FAILED,
        "SUCCESSFUL": LOG_BUSINESS_RESULT_SUCCESSFUL,
        "UNKNOWN": LOG_BUSINESS_RESULT_UNKNOWN,
        "WARNING": LOG_BUSINESS_RESULT_WARNING
    }

    LOG_EVENT_CATEGORY_DEBUG = "Debug"
    LOG_EVENT_CATEGORY_ERROR = "Error"
    LOG_EVENT_CATEGORY_INFORMATION = "Information"
    LOG_EVENT_CATEGORY_WARNING = "Warning"
    LOG_EVENT_CATEGORIES = {
        "DEBUG": LOG_EVENT_CATEGORY_DEBUG,
        "ERROR": LOG_EVENT_CATEGORY_ERROR,
        "INFORMATION": LOG_EVENT_CATEGORY_INFORMATION,
        "WARNING": LOG_EVENT_CATEGORY_WARNING
    }

    MESSAGE_ERROR_TRANSACTION_NOT_FOUND =\
        "The value 'transaction_id' could not be consulted"
    MESSAGE_ERROR_VARIABLES_TOPOLOGY =\
        "An error occurred in the processing of variables\
            for topology configuration"
    MESSAGE_ERROR_MAP = "Error in ReadingTypeCodeService.__set_codes_description,\
                error with map of reading type code"
    MESSENGER_TRANSACTION_ID_KEY = "transactionId"
    MESSENGER_USER_ID_KEY = "userId"
    MESSENGER_OWNER_KEY = "owner"

    MAP = "map"
    MAX_LENGTH = "maxLength"
    NAME_SERVICE = "MeteringSystem"
    NAME = "name"
    NUMBER = "number"

    PATTERN = "pattern"
    PRECISION = "precision"
    PROPERTIES = "properties"

    READ_FILE_OUTPUT_TYPES = ("json", "yaml")

    REQUEST_BODY_ACTION_KEY = "action"
    REQUEST_BODY_FORMULA_KEY = "formula"
    REQUEST_BODY_NAME_KEY = "name"
    REQUEST_BODY_PARAMS_KEY = "params"
    REQUEST_BODY_TRANSACTION_ID = "transactionId"
    REQUEST_BODY_SERVICE_POINT_ID = "idSpv"
    REQUEST_BODY_TAKE_KEY = "take"
    REQUEST_BODY_SKIP_KEY = "skip"
    REQUEST_BODY_FILTER_KEY = "filter"
    REQUEST_BODY_FILTERS_KEY = "filters"
    REQUEST_BODY_VARIABLE_NAME_KEY = "variableName"

    REQUEST_HEADER_OWNER_KEY = "Owner"
    REQUEST_HEADER_USER_ID_KEY = "User-Id"
    REQUEST_HEADER_TRANSACTION_ID_KEY = "Transaction-Id"
    REQUEST_HEADERS_PARAMETERS = (
        {
            "NAME": REQUEST_HEADER_OWNER_KEY,
            "GLOBAL_DATA_KEY": GLOBAL_DATA_OWNER_KEY,
            "REQUIRED": True
        },
        {
            "NAME": REQUEST_HEADER_TRANSACTION_ID_KEY,
            "GLOBAL_DATA_KEY": GLOBAL_DATA_TRANSACTION_ID_KEY,
            "REQUIRED": True
        },
        {
            "NAME": REQUEST_HEADER_USER_ID_KEY,
            "GLOBAL_DATA_KEY": GLOBAL_DATA_USER_ID_KEY,
            "REQUIRED": True
        }
    )

    REQUIRED_UDF = "required"
    RESULT_VALIDATION = "resultValidation"

    SERVICE_POINT_VARIABLE_ID_SPO_KEY = "idSpo"
    SERVICE_POINT_VARIABLE_LAST_READ_DATE_KEY = "lastReadDate"
    SERVICE_POINT_VARIABLE_METERING_TYPE_ID_DATE_KEY = "meteringTypeId"
    SERVICE_POINT_VARIABLE_SERVICE_POINT_ID_KEY = "servicePointId"
    SERVICE_POINT_VARIABLE_LOG_NUMBER_KEY = "logNumber"
    SERVICE_POINT_VARIABLE_CHANNEL_KEY = "channel"
    SERVICE_POINT_VARIABLE_RAW_DATA_KEY = "rawData"
    SERVICE_POINT_VARIABLE_RAW_READING_KEY = "rawReading"
    SERVICE_POINT_VARIABLE_USAGE_DATA_KEY = "usageData"
    SERVICE_POINT_VARIABLE_USAGE_READING_KEY = "usageReading"
    SERVICE_POINT_VARIABLE_INF_READING_KEY = "infReading"
    SERVICE_POINT_VARIABLE_YEAR_KEY = "year"

    SQS_RESOURCE_NAME = "sqs"
    STRING = "string"
    SUCCESS = "success"
    DATE_FORMAT = "%m/%d/%Y"
    TIME_FORMAT = "%m/%d/%Y %H:%M"

    UDF_INSTANCE = "udfInstance"
    USER_SYSTEM_NAME = "System"
    METERING_TYPE = "MAIN"

    UDF_NUMBER = "udfNumber"
    VARIALES_TYPES_DOMAINS_IDS = {
        "load_profile_reading": 21,
        "LOAD PROFILE READING": 21,
        "event": 22,
        "EVENTS": 22,
        "register": 23,
        "REGISTERS": 23,
        21: "LOAD PROFILE READING",
        22: "EVENTS",
        23: "REGISTERS"
    }
    VALUE = "value"

    CAST_UDF_DATATYPE_COMBINATIONS = (
        ('number', 'string'),
        ('date', 'string'),
        ('boolean', 'string'),
        ('datetime', 'string'),
        ('datetime', 'number'),
        ('date', 'number')
    )
    DELETE_UDF_DATATYPE_COMBINATIONS = (
        ('string', 'number'),
        ('string', 'datetime'),
        ('string', 'date'),
        ('string', 'boolean'),
        ('number', 'datetime'),
        ('number', 'date'),
        ('number', 'boolean'),
        ('datetime', 'boolean'),
        ('date', 'boolean'),
        ('boolean', 'number'),
        ('boolean', 'datetime'),
        ('boolean', 'date')
    )
