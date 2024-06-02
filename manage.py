#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "landingpage.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django не могу найти а вообще оно установлено?"
            "PYTHONPATH есть?"
            "виртуалка еще и не активированно?"
        ) from exc
    execute_from_command_line(sys.argv)
