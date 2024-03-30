import os

from .dev_config import DevelopmentConfig
from .prod_config import ProductionConfig

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}

def get_config():
    env = os.environ.get('FLASK_ENV', 'development')
    return config[env]
