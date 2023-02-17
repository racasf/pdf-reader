from file.directory import *
import ftplib


class FTPSender:
    def __init__(self, host, user, pwd, path):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.path = path

    def validateRequestedData(self):
        if self.host == "":
            return "Undefined FTP Host"

        if self.user == "":
            return "undefined FTP user"

        if self.pwd == "":
            return "undefined FTP password"

        if self.path == "":
            return "undefined FTP path"

        return ""

    def sendFile(self, file) -> str:
        validateData = self.validateRequestedData()
        if validateData != "":
            return validateData

        if file == "":
            return "file name undefined"

        fileName = f'/{self.path}'

        if fileName[len(fileName) - 1] != "/":
            fileName += "/"

        fileName += extractFileName(file)
        if fileName == "":
            return "we can't extract file name to send to server ({})".format(file)


        try:
            sess = ftplib.FTP(self.host, self.user, self.pwd)

            file = open(file, "rb")

            sess.storbinary(f'STOR {fileName}', file)
            file.close()
            sess.quit()

            return ""
        except Exception as i:
            return "{} [{}]".format(i, fileName)

