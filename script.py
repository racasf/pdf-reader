import config
import mailer
import PyPDF2
from file.directory import *
import pdfFile
import ftp


def main():
    print("ejecutando script")
    files = getNonProcesedFiles(config.config["origin_directory"])

    notification_success = []
    notification_error = []

    for parent in files:
        try:
            pdf_file = open(parent, "rb")
            pdfReader = PyPDF2.PdfReader(pdf_file)

            tmp_files = []

            currentClass = ""
            for i, page in enumerate(pdfReader.pages):
                txt = page.extract_text()
                if txt == "":
                    raise Exception("no pudimos leer el texto del archivo")

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

            pdf_file.close()
            changeToExecuted(parent)
        except Exception as e:
            pdf_file.close()
            notification_error.append(f'{e} [{parent}]')
            changeToError(parent)

    tmpFiles = getFilesToSend(config.dataDirectories["tmp_files"])
    ftpS = ftp.FTPSender(
        config.config["ftp_host"],
        config.config["ftp_user"],
        config.config["ftp_pwd"],
        config.config["ftp_path"]
    )

    try:
        for tf in tmpFiles:
            error = ftpS.sendFile(tf)
            if error != "":
                notification_error.append(error)

            notification_success.append(extractFileName(tf))
            deleteFileToSend(tf)
    except Exception as e:
        notification_error.append(f'Error al enviar los archivos a ftp: {e}')

    msg = mailer.prepareMessage(notification_success, notification_error)
    mailer.sendMail(msg)

