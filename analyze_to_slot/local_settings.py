import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '=!5kg%4ohchnoy4sf5)&e8+m99#hkfi=145_g#)=^4%_t@%$$$'

DATABASES = {
  'default': {
    # 既存コード
    # 'ENGINE': 'django.db.backends.sqlite3',
    # 'NAME': BASE_DIR / 'db.sqlite3',

    # herokuDB接続情報
    'ENGINE': 'django.db.backends.mysql',
    'HOST': os.getenv('DB_HOSTNAME'),
    'NAME': os.getenv('DB_NAME'),
    'USER': os.getenv('DB_USERNAME'),
    'PASSWORD': os.getenv('DB_PASSWORD'),
  }
}

DEBUG = True #ローカルでDebugできるようになります
