# Constants
REF = "$ref"
REMOVE = "$remove"

# Public classes and functions
from .abstract import YamlConfigDocument, DocReference, variable_helper
from .merger import load_subdocument
from .errors import *

__all__ = [
    'YamlConfigDocument',
    'DocReference',
    'variable_helper',
    'load_subdocument',

    'errors'
]
