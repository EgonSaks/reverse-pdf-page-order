from PyPDF2 import PdfFileWriter, PdfFileReader

output_pdf = PdfFileWriter()

with open('input.pdf', 'rb') as readfile:
    input_pdf = PdfFileReader(readfile)

    for page in reversed(input_pdf.pages):
        output_pdf.addPage(page)

    with open('output.pdf', "wb") as writefile:
        output_pdf.write(writefile)
