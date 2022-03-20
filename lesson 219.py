from PyPDF2 import PdfFileReader, PdfFileWriter

original_path = 'combined.pdf'
watermark_path = 'wtr.pdf'

with open(original_path, 'rb') as file, open(watermark_path, 'rb') as watermark:
    file_pdf = PdfFileReader(file)
    watermark_pdf = PdfFileReader(watermark)
    watermark_page = watermark_pdf.getPage(0)

    writer = PdfFileWriter()

    for i in range(file_pdf.getNumPages()):
        page = file_pdf.getPage(i)
        page.mergePage(watermark_page)
        writer.addPage(page)

    with open('watermarked.pdf', 'wb') as new_file:
        writer.write(new_file)
