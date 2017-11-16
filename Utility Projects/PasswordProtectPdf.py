#command line args use
#PasswordProtectPdf.py inputfile.pdf password output.pdf
#vinay@programmer.net


import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input = PdfFileReader(open(sys.argv[1], "rb"))
for i in range(0, input.getNumPages()):
    output.addPage(input.getPage(i))
outputStream = open(sys.argv[3], "wb")
output.encrypt(sys.argv[2], use_128bit=True)
output.write(outputStream)
outputStream.close()
