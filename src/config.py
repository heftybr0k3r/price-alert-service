import os


DEBUG = True
ADMINS = frozenset(
    [
        os.env.get("ADMIN_EMAIL")
    ]
)
