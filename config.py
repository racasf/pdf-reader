import os
import configparser
from platformdirs import *

initScript = """
    Developed by RACA Software Factory
"""

APPNAME: str = "pdf-exporter"
APPAUTHOR: str = "RACA Software Factory"

configInput = {
    "origin_directory": "Ingrese el directorio de origen [{}]: ",
    # "smtp_host": ""
    # "smtp": {
    #     "user": "",
    #     "pass": "",
    #     "host": "",
    #     "port": ""
    # },
    # "notification_emails": {}
}

config = {
    "origin_directory": "",
    # "smtp_host": ""
}

dataDirectories = {
    "user": user_data_dir(APPNAME, APPAUTHOR),
    "user_cache": user_cache_dir(APPNAME, APPAUTHOR),
    "user_log": user_log_dir(APPNAME, APPAUTHOR),
    "user_docs": user_documents_dir(),
    "runtime": user_runtime_dir(APPNAME, APPAUTHOR)
}

def createAppDirectories():
    for dir in dataDirectories:
        os.makedirs(dataDirectories[dir], exist_ok=True)


def getFilePath() -> str:
    return "{}/config.ini".format(dataDirectories["user"])


def createConfigFile():
    cnf = configparser.ConfigParser()

    with open(getFilePath(), "w") as fo:
        cnf.write(fo)


def requestData() -> config:
    for x in configInput:
        data = input(configInput[x].format(config[x]))
        if data is not "":
            config[x] = data

    return config

def writeConfig():
    cnf = configparser.ConfigParser()

    for d in config:
        cnf["DEFAULT"][d] = config[d]

    with open(getFilePath(), "w") as fo:
        cnf.write(fo)

def readConfigFile():
    cnf = configparser.ConfigParser()

    cnf.read(getFilePath())

    for d in config:
        if not cnf.has_option("DEFAULT", d):
            cnf["DEFAULT"][d] = config[d]
        else:
            config[d] = cnf["DEFAULT"][d]
