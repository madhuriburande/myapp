class Config(object):
    """
    common configuration
    """

    # put any configuration here that are common across all environments

    SECRET_KEY = 'abcdefghi789'
    # SQLALCHEMY_DATABASE_URI = '<use_database>://<username>:<password>@<IP>/<database_name>'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/emp_info'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    """
    testing

     Configuration
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:localhost/student_info1_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Production Configuration
    """

    DEBUG = False


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
