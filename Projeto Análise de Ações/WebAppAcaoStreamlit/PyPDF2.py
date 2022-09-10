#pip3 install pyPdf
#pip install PyPDF2
import PyPDF2

#C:\Users\tamar\Downloads\Nota
#Abrindo o PDF
pdf_file = open("Nota.pdf", "rb")

dados_do_pdf = PyPDF2.PdfFileReader(pdf_file)

n = dados_do_pdf.numPages
#print('Números de paginas' + str(dados_do_pdf.numPages))
#Setando a variavel pagina com o objeto pagina1
#pagina1 = dados_do_pdf.getPage(0)
#texto_da_pagina1 = pagina1.extractText()
#print(texto_da_pagina1)
#n = pdf_reader.numPages
for i in range(0, n):
    print("Página {}".format(1+i))
    page = pdf_reader.getPage(i)
    print(page.extractText())


class PdfFileReader:
    pass