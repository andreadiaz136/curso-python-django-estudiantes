r"""
Ajustes the debug
"""
from .comunes import *
try:
    from .host import *
except ImportError:
    ...

ENTORNO = 'Estoy en modo Debug'

DEBUG = True

ALLOWED_HOSTS = ['*']



