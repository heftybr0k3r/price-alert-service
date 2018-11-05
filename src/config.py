import os

__author__ = "Zexx"

DEBUG = True
ADMINS = frozenset(
    [
        os.environ.get("ADMIN_EMAIL")
    ]
)
