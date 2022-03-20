import sys
import PyPDF2


def pdf_rotater(in_path, out_path, deg):
    with open(in_path, 'rb') as file:
        page_reader = PyPDF2.PdfFileReader(file)
        page = page_reader.getPage(0)
        page.rotateClockwise(deg)
        page_writer = PyPDF2.PdfFileWriter()
        page_writer.addPage(page)
        with open(out_path, 'wb') as new_file:
            page_writer.write(new_file)


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for file in pdf_list:
        merger.append(file)
    merger.write('PDFwatermark\combined.pdf')


inputs = sys.argv[1:]
pdf_combiner(inputs)
pdf_rotater('PDFwatermark\\dummy.pdf', 'PDFwatermark\\tilted.pdf', 90)
