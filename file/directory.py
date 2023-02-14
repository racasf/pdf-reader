import os
import re

import config

REGEXP_ERROR = "error - "
REGEXP_EXECUTED = "executed - "

def getPathWithFile(path: str, file: str) -> str:
    if path[len(path) - 1] == "/":
        return path + file
    else:
        return path + "/" + file


def getNonProcesedFiles(path: str):
    files = []
    for f in os.listdir(path):
        fname = getPathWithFile(path, f)
        if not os.path.isfile(fname):
            continue

        if isIgnoredFile(fname):
            continue

        files.append(fname)
    return files

def isIgnoredFile(file: str) -> bool:
    if isErrorFile(file):
        return True

    if isExecutedFile(file):
        return True
    return False


def isErrorFile(file: str) -> bool:
    return re.search(REGEXP_ERROR, file) is not None


def isExecutedFile(file: str) -> bool:
    return re.search(REGEXP_EXECUTED, file) is not None


def changeToError(file: str):
    fnameArray = file.split("/")
    fname = fnameArray[len(fnameArray) - 1]
    absolutePath = fnameArray[:len(fnameArray) - 1]

    newName = "/".join(absolutePath) + "/" + REGEXP_ERROR + fname

    os.rename(file, newName)
    return


def changeToExecuted(file: str):
    fnameArray = file.split("/")
    fname = fnameArray[len(fnameArray) - 1]
    absolutePath = fnameArray[:len(fnameArray) - 1]

    newName = "/".join(absolutePath) + "/" + REGEXP_EXECUTED + fname

    os.rename(file, newName)
    return