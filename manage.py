#!/usr/bin/env python
# manage.py
# Django default management commands, with some special sauce.
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Tue Jan 19 20:52:05 2016 -0500
#
# Copyright (C) 2015 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: manage.py [] benjamin@bengfort.com $

"""
Django default management commands, with some special sauce.
"""

##########################################################################
## Imports
##########################################################################


import os
import sys
import dotenv

##########################################################################
## Main Method
##########################################################################

if __name__ == "__main__":
    ## Manage Django Environment
    if os.path.exists('.env'):
        dotenv.read_dotenv()

    ## Set the default settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finances.settings")

    ## Execute Django utility
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
