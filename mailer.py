import smtplib, ssl
import config

config.readConfigFile()
cnf = {
    "port": config.config.get("email_smtp_port"),
    "host": config.config.get("email_smtp_host"),
    "mail": config.config.get("email_account"),
    "pass": config.config.get("email_password"),
    "dest": config.config.get("email_avisos")
}

def validateConfig():
    for x in cnf:
        if cnf[x] == "":
            return False
    return True

def prepareMessage(notificaciones: list, errores: list) -> str:
    message = "Subject: PDF Exporter - Avisos y Notificaciones\n\n"

    message += "Notificaciones:\n"
    for m in notificaciones:
        message += "- {}\n".format(m)

    message += "\nErrores:\n"
    for m in errores:
        message += "- {}\n".format(m)
    return message

def sendMail(message: str):
    vc = validateConfig()
    if not vc:
        return

    context=ssl.create_default_context()

    try:
        server = smtplib.SMTP_SSL(cnf["host"], cnf["port"], context=context)
        server.login(cnf["mail"], cnf["pass"])
        server.sendmail(cnf["mail"], cnf["dest"], message)

    except Exception as e:
        print(e)
