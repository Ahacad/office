
#%%
def split(path, nameOfSplit):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        
        output = f'{nameOfSplit}{page}.pdf'
        with open(output, 'wb') as outputPdf:
            pdf_writer.write(outputPdf)
    
    return pdf.getNumPages()

#%%
def mergePdfs(paths, output):
    pdfWriter = PdfFileWriter()
    
    output = output + '.pdf'
    for path in paths:
        pdfReader = PdfFileReader(path)
        for page in range(pdfReader.getNumPages()):
            pdfWriter.addPage(pdfReader.getPage(page))
        
        
        with open(output, 'wb') as out:
            pdfWriter.write(out)
#%%
def inputNames():
    path = ''
    while '.pdf' not in path:
        print('please put the pdf in the same folder with the python programme!')    
        path = input('please type in its name(including.pdf):     ')
    start = int(input('iniput the start number of the files:   '))
    end = int(input('input the end number of the files:  '))    
    output = input('chose the name for the merged pdf:   ')
    return path, start, end, output
#%%
def deleteFiles(path, pageNumber):
    print("if you want to delete the generated files please type '1'")
    judge = int(input('type here:   '))
    if judge == 1:
        for i in range(pageNumber):
            os.remove(path[:-4]+str(i)+'.pdf')
#%%
def main():
    sure = False
    while sure == False:
        path, start, end, output = inputNames()
        print("if you are sure please type '1', if you want to make some changes please type '0'")
        judge = int(input('type here:   '))
        if judge == 1:
            sure = True
        elif judge == 0:
            sure = False
        else:
            print('invalid input!!!')
    
    nameOfSplit = path[:-4]
    pageNumber = split(path, nameOfSplit)
    
    paths = []
    for i in range(start, end+1):
        paths.append(nameOfSplit+str(i)+'.pdf')
    
    mergePdfs(paths, output)
                
    deleteFiles(path, pageNumber)
    
if __name__ == '__main__':
    from PyPDF2 import PdfFileReader, PdfFileWriter
    import os
    main()
#%%

#%%
