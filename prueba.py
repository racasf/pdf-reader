# # import PyPDF2
# #
# # pdfFileObj = open("pdf-1.pdf", "rb")
# #
# # pdfReader = PyPDF2.PdfReader(pdfFileObj)
# #
# # print(len(pdfReader.pages))
# #
# # pageObj = pdfReader.pages[1]
# #
# # txt = pageObj.extract_text()
# # print(txt)
# #
# #
# #
# # pdfFileObj.close()
# from src.dir_reader.dir_reader import dirReader
#
#
# def main():
#     d = dirReader("./")
#
#     f = d.getAllPDFFiles()
#     print(f)
#
# main()