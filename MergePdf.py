import PyPDF2

pdfiles = ["one.pdf","two.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    pdFile = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdFile)
    merger.append(pdfReader)

pdFile.close()
merger.write('merger.pdf')