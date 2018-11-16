#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "connectedin.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exercicios.settings")
>>>>>>> 0d9c146d35a01c6c0e71a84ee143bbd9685b2080
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
