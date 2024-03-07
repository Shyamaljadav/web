import os
from deta import Deta
from dotenv import load_dotenv


load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

deta = Deta(DETA_KEY)

# This is how to create/connect a database
ur = deta.Base("users_db")


def insert_user(username, name, password):
    """Returns the user on a successful user creation, otherwise raises and error"""
    return ur.put({"key": username, "name": name, "password": password})


def fetch_all_users():
    """Returns a dict of all users"""
    res = ur.fetch()
    return res.items


def get_user(username):
    """If not found, the function will return None"""
    return ur.get(username)


def update_user(username, updates):
    """If the item is updated, returns None. Otherwise, an exception is raised"""
    return ur.update(updates, username)


def delete_user(username):
    """Always returns None, even if the key does not exist"""
    return ur.delete(username)


