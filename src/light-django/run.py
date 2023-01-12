from django.core.management import execute_from_command_line
import os
import sys


argv = sys.argv.copy()

if len(argv) == 1:  # run directly
    argv.append("runserver")

# load settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# run
execute_from_command_line(argv)
