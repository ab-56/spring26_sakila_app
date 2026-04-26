
import os

class Config:
    MYSQL_HOST = os.environ.get("MYSQL_HOST", "db")
    MYSQL_USER = os.environ.get("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD", "admin")
    MYSQL_DB = os.environ.get("MYSQL_DATABASE", "sakila")
    SECRET_KEY = "dev"