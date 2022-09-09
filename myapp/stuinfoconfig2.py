class Config(object):
    """
    common configuration
    """

    # put any configuration here that are common across all environments

    SECRET_KEY = 'abcdefghi789'
    # SQLALCHEMY_DATABASE_URI = '<use_database>://<username>:<password>@<IP>/<database_name>'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/student_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class Testing(Config):
    """
    testing

     Configuration
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:localhost/testing_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    """
    Production Configuration
    """

    DEBUG = False


app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}
