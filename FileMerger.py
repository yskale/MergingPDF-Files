'''
Author: YSK      Date 8/4/2017
Package Installation : Package required for this file is PyPDF2 and can be installed on command prompot as  'pip install PyPDF2'.
Instruction: Execute (Double Click ) the mergefile.py file in the directory containing all pdf files to be summarized.
Aim: To extract the first two pages from each pdf file and then combine them to one file.
Input: PDF files 
Output:Mergefile is the PDF file having n number given pages from each pdf file in that folder.  

'''
import PyPDF2, os
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()
for filename in pdfFiles:
    if filename != ('Mergedfile.pdf'): #Name of Output file
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        numberofpages = input("Enter number of pages to be extracted from each documents") 
        for pagenum in range(0,numberofpages): #Number of pages required from each documents. Here 0,2 means first and second page of each document
            pageObj = pdfReader.getPage(pagenum)
            pdfWriter.addPage(pageObj)
pdfOutput = open('Mergedfile.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
