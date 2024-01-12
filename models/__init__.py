#!/usr/bin/python3
""" It initializes the storage model. """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
