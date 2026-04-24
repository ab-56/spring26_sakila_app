# Name: Abeeha Maryam
# Date: 2026-04-24

import os

MYSQL_HOST = 'db-primary'

HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))