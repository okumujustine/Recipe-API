"""
Django command to wait for the database to be available
"""
import time

from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError


class Command(BaseCommand):
    """ Wait for the database to be available"""

    def handle(self, *args, **options):
        """entry point for command"""
        self.stdout.write("Waiting for database ....")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database not available, waiting one second")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available"))
