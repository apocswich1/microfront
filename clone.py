import os
import time
import shutil
from git import Repo

#directorio = os.listdir("./")
directorio = ("./main/mf-main/")
directorio2 = ("./main/mf-main/src/")
path = ("./main/mf-main/")
s = input("Enter project name to create MF: (default = mf-module) ")

milista = [
    "./main/mf-main/angular.json",
    "./main/mf-main/package.json",
    "./main/mf-main/package-lock.json",
    "./main/mf-main/src/main.single-spa.ts",
    "./main/mf-main/src/set-public-path.js",
    "./main/mf-main/src/app/app.component.spec.ts",
    "./main/mf-main/src/app/app.component.ts"
]

if s == "":
    s = "mf-module"
    titulo = "modulo"
else:
    titulo = s
    s = "mf-"+s

def listar_archivos(nombre):
    otropath = "./"+nombre
    pathnuevo = os.listdir(otropath)
    for i in range(len(pathnuevo)):
        if os.path.isdir(pathnuevo[i]) and not pathnuevo[i].find("./././mf-main/node_module") and not pathnuevo[i].find(".git") and not pathnuevo[i].find(".angular"):
            print("---"+pathnuevo[i])
            listar_archivos(os.listdir(pathnuevo[i]))
        else:
            # Open a file
            print("-open:--"+pathnuevo[i])
            if os.path.isdir("./"+nombre+"/"+pathnuevo[i]):
                print("-ENTRADA es directorio:--"+"./"+nombre+"/"+pathnuevo[i])
                listar_archivos("./"+nombre+"/"+pathnuevo[i])
            else:
                print("-ENTRADA #####:--"+"./"+nombre+"/"+pathnuevo[i])
                entrada = open("./"+nombre+"/"+pathnuevo[i],  encoding='latin-1').read()
                out = open("./"+nombre+"/"+pathnuevo[i], 'w')
                replacements = {'mf-main':s}
            
                for e in replacements.keys():
                    entrada = entrada.replace(e, replacements[e])
                out.write(entrada)
                out.close
                print("---"+pathnuevo[i])

def reemplazar(nombre):
    #print("-ENTRADA:--"+"./"+nombre)
    entrada = open("./"+nombre).read()
    out = open("./"+nombre, 'w')
    replacements = {'mf-main':s}   
    for i in replacements.keys():
        entrada = entrada.replace(i, replacements[i])
    out.write(entrada)
    out.close

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()

items = list(range(0, 57))
l = len(items)

print("1- Starting project...")
print("2- Cloning process...")
#print("3- Reading directories.../n")
#printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
#os.rename('./main/mf-main/node_modules','./main/mf-main/node_modules') 
#for i in range(len(directorio)):
    #if not directorio[i]=="clone.py" and not directorio[i]==".DS_Store" and not directorio[i]=="." and not directorio[i]=="..":
     #   if os.path.isdir(directorio[i]):
    #        print("--"+directorio[i])
   #         otro = directorio[i]
#            listar_archivos(otro)
 #       else:
  #          print("-"+directorio[i])
 #           reemplazar(directorio[i])

for i in range(len(milista)):
    reemplazar(milista[i])
    print("-"+milista[i])

os.rename('./main/mf-main','./main/'+s)
os.rename('./main','./'+titulo)  
#os.rename('./main/mf-main/node_modules','./main/mf-main/node_modules') 

for item in progressBar(items, prefix = 'Progress:', suffix = 'Complete', length = 50):
    # Do stuff...
    time.sleep(0.05)

print("-- Clone ready --")
