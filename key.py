import streamlit_authenticator as stauth
import database as db
import pickle
import pathlib as ph

names = ["shiv"]
usernames = ["shyamal"]
passwords = ["123"]
email = ["test@gmail.com"]

hashed_passwords = stauth.Hasher(passwords).generate()
credentials = {"usernames":{}}

for un, name, pw in zip(usernames, names, passwords):
    user_dict = {"name":name,"password":pw}
    credentials["usernames"].update({un:user_dict})

    converterkey=' BgvHf7Kuy9FWFR644bq8SDK3Td5lOY6x '




