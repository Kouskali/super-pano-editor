from tkinter.filedialog import *
import pickle

def getfilepath(head):
    filepath = askopenfilename(title=head,filetypes=[('configuration super pano','.supano'),('all files','.*')])
    return filepath
    
def readfilecontent():

    Fichier = open(getfilepath("Ouvrir un fichier de configuration"),'r')
    cachedata = Fichier.read()
    return cachedata
    
    
def writefilecontent(cachedata):

    Fichier = open(getfilepath("Enregistrer un fichier de configuration"),'w')
    Fichier.write(cachedata)