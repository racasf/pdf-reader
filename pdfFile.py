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