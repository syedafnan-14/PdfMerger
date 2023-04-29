# PdfMerger
This Python program uses the PyPDF2 library to merge two PDF files into a single PDF file. The program starts by importing the PyPDF2 library. The names of the PDF files to be merged are stored in a list called `pdfiles`. Then, a `PdfMerger` object is created to merge the PDF files.

Next, a loop is used to iterate through the `pdfiles` list. For each file in the list, the program opens the file in read-binary mode using the `open` function and reads the PDF using the `PdfFileReader` function of PyPDF2 library. Then, the `append` method of the `PdfMerger` object is used to append the PDF file to the `merger`.

After all the files have been appended, the program closes the files using the `close` method and writes the merged PDF file to a new file called `merger.pdf` using the `write` method of the `PdfMerger` object.

To use this program, you need to have PyPDF2 library installed on your system. You can install it using pip by running the command `pip install PyPDF2` in your terminal or command prompt. Then, save this program with the filename of your choice with the `.py` extension, and run the program using the command `python filename.py` in your terminal or command prompt. The merged PDF file will be saved in the same directory as the program.
