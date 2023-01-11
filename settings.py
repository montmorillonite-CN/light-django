# configs for changing between dev. & prod.
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1"]

# secret_key, do NOT let others knows.
SECRET_KEY = "1145141919810"

# locale configs, take `Chinese` as an example.
LANGUAGE_CODE = "zh-hans"
TIME_ZONE = "UTC+8"

# WARNING: configs below should NOT be changed
#          unless you know what are you doing.
ROOT_URLCONF = "urls"
WEBSITE_FOLDER = "website"
