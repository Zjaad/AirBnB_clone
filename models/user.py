#!/usr/bin/python3

"""Defines the User class(his email,password & name)."""

from models.base_model import BaseModel


class User(BaseModel):
    """Representing a User."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
