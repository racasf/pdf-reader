import time

import config
import schedule
from script import *

print(config.initScript)

value = input("Presione cualquier tecla + enter para iniciar la configuración o presione enter: ")

if value == "":
    @schedule.repeat(schedule.every(5).minutes)
    def executeMainFunction():
        main()

    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    config.createAppDirectories()

    config.readConfigFile()

    config.requestData()

    config.writeConfig()

