import os
import configparser
from platformdirs import *
import config

print(config.initScript)

config.createAppDirectories()

config.readConfigFile()

config.requestData()

config.writeConfig()

