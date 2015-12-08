"""Vscale API"""

__version__ = "1.0"
__author__ = "Rogachev Sergey ( https://github.com/redknife )"
__author_email__ = "redknife183@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2015 Rogachev Sergey"

from .Manager import Manager
from .Account import Account
from .Scalet import Scalet
from .baseapi import Error, TokenError, DataReadError