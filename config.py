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

    "email_account": "Ingrese la cuenta de email remitente [{}]: ",
    "email_password": "Ingrese la contraseña de la cuenta de email remitente [{}]: ",
    "email_smtp_host": "Ingrese el host SMTP del mail [{}]: ",
    "email_smtp_port": "Ingrese el puerto SMTP del mail [{}]: ",

    "email_avisos": "Ingrese el email para avisos y notificaciones [{}]: ",

    "ftp_host": "Ingrese el host de FTP [{}]: ",
    "ftp_user": "Ingrese el user para FTP [{}]: ",
    "ftp_pwd": "Ingrese el pwd para FTP [{}]: ",
    "ftp_path": "Ingrese el path default para FTP [{}]: "
}

config = {
    "origin_directory": "",

    "email_account": "",
    "email_password": "",
    "email_smtp_host": "",
    "email_smtp_port": "",

    "email_avisos": "",

    "ftp_host": "",
    "ftp_user": "",
    "ftp_pwd": "",
    "ftp_path": ""
}

dataDirectories = {
    "user": user_data_dir(APPNAME, APPAUTHOR),
    "tmp_files": user_data_dir(APPNAME, APPAUTHOR) + "/tmp/",
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
        if data != "":
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
