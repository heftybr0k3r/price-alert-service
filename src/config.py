import os


DEBUG = True
ADMINS = frozenset( #unordered
    [
        os.env.get("ADMIN_EMAIL")
    ]
)
