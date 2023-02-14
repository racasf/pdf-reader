import re

GUIA_REGEXP = "(([A-Z8]{3})+([0-9]{5,8}))"

class pdfFile:
    def __init__(self, parentFile: str):
        self.parentFile = str
        self.fileName = ""
        self.sheetsNumber = []

    def setSheetNumber(self, number: int):
        self.sheetsNumber.append(number)

    def setFileName(self, filename: str):
        self.fileName = filename

    def getSheetNumber(self) -> list:
        return self.sheetsNumber


def getGuiaNumber(txt: str):
    name = ""
    fnd = re.findall(GUIA_REGEXP, txt)
    if len(fnd) > 0:
        name = fnd[0][0]
    return name