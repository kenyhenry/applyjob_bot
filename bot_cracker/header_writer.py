from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import RectangleObject

def writeCrackCv():
    writer = PdfFileWriter() 
    reader = PdfFileReader(open('./cv_khy_french_2022.pdf', 'rb')) 
    linkfrom = writer.addPage(reader.getPage(0))
    linkto = writer.addPage(reader.getPage(1))

    output = open('keny_henry.pdf','wb') 
    writer.write(output) 
    output.close() 