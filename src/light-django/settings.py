# configs for changing between dev. & prod.
DEBUG = True
ALLOWED_HOSTS = ["*"]

# secret_key, do NOT let others knows.
SECRET_KEY = "4de65c187393c1e50d4c59deeff954f7"

# locale configs, take `Chinese` as an example.
LANGUAGE_CODE = "zh-hans"
TIME_ZONE = "Asia/Shanghai"

# WARNING: configs below should NOT be changed
#          unless you know what are you doing.
ROOT_URLCONF = "urls"
WEBSITE_FOLDER = "website"
