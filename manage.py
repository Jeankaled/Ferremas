#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import cx_Oracle,os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferremas.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


cx_Oracle.init_oracle_client(lib_dir=r'C:\Users\jeana\Desktop\Ferremas\wallet')