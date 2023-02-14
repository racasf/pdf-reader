import config
import mailer
import PyPDF2
from file.directory import *
import pdfFile

print(config.initScript)

files = getNonProcesedFiles(config.config["origin_directory"])

for parent in files:
    pdf_file = open(parent, "rb")
    pdfReader = PyPDF2.PdfReader(pdf_file)

    tmp_files = []

    currentClass = ""
    for i, page in enumerate(pdfReader.pages):
        # si es una guia creamos una nueva clase y cerramos y mergeamos la anterior la anterior
        txt = page.extract_text()
        pageNumber = i+1
        guiaNumber = pdfFile.getGuiaNumber(txt)

        if guiaNumber is not "":
            if currentClass is not "":
                tmp_files.append(currentClass)

            currentClass = pdfFile.pdfFile(parent)
            currentClass.setFileName(guiaNumber)

        currentClass.setSheetNumber(pageNumber)

    if currentClass is not "":
        tmp_files.append(currentClass)

    print(len(tmp_files))
    # analizamos los archivos para crear los pdf files

    # creamos los archivos pdf separando del original

    # cambiamos el nombre del archivo

# enviamos los archivos al servidor

# iteramos sobre cada archivo

    # enviamos al servidor

    # si se envia lo borramos

    # si no envia lo agregamos al mail

# enviamos el mail
# msg = mailer.prepareMessage({"Se exportaron 967 archivos"}, {"Fallaron 12"})
#
# mailer.sendMail(msg)