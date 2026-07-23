"""
P.I.E. Configuration Manager
"""

import json
import os


CONFIG_FILE = "config/default.json"


class Config:


    def __init__(self):
        self.data = {}
        self.load()


    def load(self):

        if not os.path.exists(CONFIG_FILE):
            self.data = {}
            return


        with open(CONFIG_FILE, "r") as file:
            self.data = json.load(file)


    def get(self, section, key):

        try:
            return self.data[section][key]

        except KeyError:
            return None


    def set(self, section, key, value):

        if section not in self.data:
            self.data[section] = {}

        self.data[section][key] = value


    def save(self):

        with open(CONFIG_FILE, "w") as file:
            json.dump(
                self.data,
                file,
                indent=4
            )
