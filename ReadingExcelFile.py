import openpyxl, PyPDF2
import os
#////Permission denied for reading and writing in PDF
# wb = openpyxl.load_workbook('Book.xlsx')
# print(type(wb))

# print(wb.sheetnames)

# sheet=wb["Sheet1"]
# print(sheet)

# print(sheet['A1'].value)

os.chdir("C:\\Users\\kanaw\\OneDrive\\Desktop\\Smita")
pdfFile=open("git-cheat-sheet-education.pdf",'rb')
pdf1File=open("git-cheat-sheet-education1.pdf",'rb')
reader1=PyPDF2.PdfReader(pdfFile)
reader2=PyPDF2.PdfReader(pdf1File)

writer=PyPDF2.PdfWriter()
for pageNum in range(len(reader1.pages)):
    page=reader1.pages[pageNum]
    writer.add_page(page)
    
for pageNum in range(len(reader2.pages)):
    page=reader2.pages[pageNum]
    writer.add_page(page)

outputPdfFile=open("OutputFile.pdf",'wb')
writer.write(outputPdfFile)
outputPdfFile.close()
pdf1File.close()
pdfFile.close()

