import PyPDF2
import re

pdf_file = open('./cv_khy_french_2022.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
print(number_of_pages)
for x in range(0, number_of_pages):
    page = read_pdf.getPage(x)
    page_content = page.extractText()
    print (page_content)
    for match in re.finditer("c\+\+", page_content):
        print("----------------found---------------")