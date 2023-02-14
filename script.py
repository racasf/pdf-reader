import config
import mailer
import PyPDF2
from file.directory import *
import pdfFile

print(config.initScript)

files = getNonProcesedFiles(config.config["origin_directory"])

notification_success = []
notification_error = []

for parent in files:
    pdf_file = open(parent, "rb")
    pdfReader = PyPDF2.PdfReader(pdf_file)

    tmp_files = []

    currentClass = ""
    for i, page in enumerate(pdfReader.pages):
        # si es una guia creamos una nueva clase y cerramos y mergeamos la anterior la anterior
        txt = page.extract_text()
        pageNumber = i
        guiaNumber = pdfFile.getGuiaNumber(txt)
        if guiaNumber != "":
            if currentClass != "":
                tmp_files.append(currentClass)

            fileName = config.dataDirectories["tmp_files"] + guiaNumber + ".pdf"
            currentClass = pdfFile.pdfFile(parent)
            currentClass.setFileName(fileName)

        currentClass.setSheetNumber(pageNumber)

    if currentClass != "":
        tmp_files.append(currentClass)

    for tf in tmp_files:
        writer = PyPDF2.PdfWriter()
        for page in tf.getSheetNumber():
            writer.add_page(pdfReader.pages[page])

        with open(tf.fileName, 'wb') as file:
            writer.write(file)

    changeToExecuted(parent)

# enviamos los archivos al servidor

# iteramos sobre cada archivo

    # enviamos al servidor

    # si se envia lo borramos

    # si no envia lo agregamos al mail

# enviamos el mail
# msg = mailer.prepareMessage({"Se exportaron 967 archivos"}, {"Fallaron 12"})
#
# mailer.sendMail(msg)

