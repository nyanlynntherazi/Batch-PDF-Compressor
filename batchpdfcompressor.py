import os
import subprocess

dir = '<path to directory>'
for path,dirs,files in os.walk(dir):
    for file in files:
        if file.endswith(".pdf"):
            filename = os.path.join(path,file)
            print(filename)
            arg1= '-sOutputFile='+file #added a c to the filename
            p = subprocess.Popen(['gs','-sDEVICE=pdfwrite', 
            					'-dCompatibilityLevel=1.4', 
            					'-dPDFSETTINGS=/screen', #Change Accordingly: Description Below
            					'-dNOPAUSE','-dBATCH', 
            					'-dQUIET', str(arg1), filename], 
                                 stdout=subprocess.PIPE)
            print (p.communicate())
            print (file + 'XXX')

#/screen selects low-resolution output similar to the Acrobat Distiller "Screen Optimized" setting.
#/ebook selects medium-resolution output similar to the Acrobat Distiller "eBook" setting.
#/printer selects output similar to the Acrobat Distiller "Print Optimized" setting.
#/prepress selects output similar to Acrobat Distiller "Prepress Optimized" setting.
#/default selects output intended to be useful across a wide variety of uses, possibly at the expense of a larger output file.
