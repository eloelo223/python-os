import os,shutil
nazwa = input("jaka nazwa pliku wariacie?")

nazwa2 = input("jaka chcesz nazwe?")

plik=input("gdzie trzymasz plik desktop, downloads,documents,imagines")

if plik == 'desktop':   
    os.rename("C:/Users/pawel/OneDrive/Desktop/"+nazwa,"C:/Users/pawel/OneDrive/Desktop/"+nazwa2)

if plik == 'downloads':
    os.rename("C:/Users/pawel/Downloads/"+nazwa,"C:/Users/pawel/Downloads/"+nazwa2)

if plik == 'dosuments':
    os.rename("C:/Users/pawel/OneDrive/Documents/"+nazwa,"C:/Users/pawel/OneDrive/Documents/"+nazwa2)
    
if plik == "imagines":
    os.rename("C:/Users/pawel/OneDrive/Obrazy/"+nazwa,"C:/Users/pawel/OneDrive/Obrazy/"+nazwa2)

y_n = input("czy chcesz cos usunąć? y/n")

if y_n == 'y':
    e = input("jaki plik chcesz usunąć? podaj lokalizację i nazwe")
    shutil.rmtree(e)

else:
    exit()