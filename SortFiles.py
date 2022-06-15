

import os
import time


#the directory you want sorted --------------

inputDir = input("Enter the directory you want to sort: ") #promting user to enter directory

print('-------------------------------------------------\n Available languages:\n en=English\n sv=Svenska\n-------------------------------------------------')

folderLanguage = input("In what language do you want the folder names?:") #promting user to enter directory

parent_dir = (inputDir+ '/')

#parent_dir = "C:/users/filip/downloads/PythonTest/" #permanent directory


#directory names SWEDISH --------------------------

if folderLanguage == 'SV' or folderLanguage == 'sv':
    directoryMovies = 'Filmer'
    directoryPictures = 'Bilder'
    directoryDocuments = 'Dokument'
    directorySetupFiles = 'Installationsfiler'
    directoryCompressed = 'Komprimerade Filer'
    directoryPhotoshop = 'Photoshop'
    directoryModels = '3d-modeller'
    directorySounds = 'Ljudfiler'
    directoryTorrents = 'Torrents'
    directoryISOfiles = 'ISO-filer'
    directoryPython = 'Python'
    directoryConfigs = 'Konfigurationer'
    directoryLogs = 'Loggar'
    directoryText = 'Textfiler'
    directoryRemoteDesktop = 'Remote desktop'
    directoryWeb = 'Web-filer'
    
elif folderLanguage == 'EN' or folderLanguage == 'en':
    directoryMovies = 'Movies'
    directoryPictures = 'Pictures'
    directoryDocuments = 'Documents'
    directorySetupFiles = 'Installation-files'
    directoryCompressed = 'Compressed-files'
    directoryPhotoshop = 'Photoshop'
    directoryModels = '3d-models'
    directorySounds = 'Sound-files'
    directoryTorrents = 'Torrents'
    directoryISOfiles = 'ISO-files'
    directoryPython = 'Python'
    directoryConfigs = 'Config-files'
    directoryLogs = 'Log-files'
    directoryText = 'Text-files'
    directoryRemoteDesktop = 'Remote desktop'
    directoryWeb = 'Web-files'


else:
    print('Language not supported')
    input("Press any key to exit...")
    exit()


#creates movies folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryMovies)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryMovies)
except: 
    print("Folder '% s' already exists" % directoryMovies) 



#creates picture folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryPictures)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryPictures)
except: 
    print("Folder '% s' already exists" % directoryPictures) 



#creates pdf folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryDocuments)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryDocuments)
except: 
    print("Folder '% s' already exists" % directoryDocuments)


#creates installers folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directorySetupFiles)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directorySetupFiles)
except: 
    print("Folder '% s' already exists" % directorySetupFiles)


#creates compressed folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryCompressed)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryCompressed)
except: 
    print("Folder '% s' already exists" % directoryCompressed)


#creates photoshop folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryPhotoshop)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryPhotoshop)
except: 
    print("Folder '% s' already exists" % directoryPhotoshop)


#creates models folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryModels)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryModels)
except: 
    print("Folder '% s' already exists" % directoryModels)


#creates sounds folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directorySounds)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directorySounds)
except: 
    print("Folder '% s' already exists" % directorySounds)


#creates torrents folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryCompressed)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryCompressed)
except: 
    print("Folder '% s' already exists" % directoryCompressed)


#creates ISOfiles folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryISOfiles)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryISOfiles)
except: 
    print("Folder '% s' already exists" % directoryISOfiles)


#creates python folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryPython)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryPython)
except: 
    print("Folder '% s' already exists" % directoryPython)


#creates configs folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryConfigs)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryConfigs)
except: 
    print("Folder '% s' already exists" % directoryConfigs)


#creates logs folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryLogs)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryLogs)
except: 
    print("Folder '% s' already exists" % directoryLogs)


#creates Textfiles folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryText)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryText)
except: 
    print("Folder '% s' already exists" % directoryText)


#creates remote desktop folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryRemoteDesktop)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryRemoteDesktop)
except: 
    print("Folder '% s' already exists" % directoryRemoteDesktop)


#creates webbfiles folder -------------------------

time.sleep(0.1)

dir = os.path.join(parent_dir, directoryWeb)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryWeb)
except: 
    print("Folder '% s' already exists" % directoryWeb)



time.sleep(0.1)

dir = os.path.join(parent_dir, directoryTorrents)

try:
    os.mkdir(dir)
    print("Folder '% s' created" % directoryTorrents)
except: 
    print("Folder '% s' already exists" % directoryTorrents)



time.sleep(1)






#file sorting -------------------------------------------

import glob
import shutil
from os import path
filename=glob.glob(parent_dir+ '/*')

documents=['.pdf','.PDF','.docx','.doc','.xlsx','.xls']
pictures=['.jpeg','.jpg','.svg','.png','.PNG','.gif','.JPG','.heic']
movies=['.mp4','.flv','.gifv','.mov','.qt','.mpeg','m4v','flv']
installers=['.exe','.msi']
compressedFiles=['.zip','.z7']
photoshop=['.psd','.psdc']
models=['.stl','.STL','.skp','.gcode','.stp','.fbx','.obj']
sounds=['.mp3','.m4a','.flac','.wav','.wma','.aac']
torrents=['.torrent','.7z.torrent']
ISOfiles=['.iso','.ISO']
python=['.py']
configs=['.conf','.CFG','.cfg']
logs=['.log']
text=['.txt']
RemoteDesktop=['.rdp']
Web=['.html','.php','.css']

DocumentsLocation=(parent_dir+ directoryDocuments)
MovieLocation=(parent_dir+ directoryMovies)
PictureLocations=(parent_dir+ directoryPictures)
SetupFilesLocation=(parent_dir+ directorySetupFiles)
CompressedFilesLocation=(parent_dir+ directoryCompressed)
PhotoshopFilesLocation=(parent_dir+ directoryPhotoshop)
ModelFilesLocation=(parent_dir+ directoryModels)
SoundFilesLocation=(parent_dir+ directorySounds)
TorrentFilesLocation=(parent_dir+ directoryTorrents)
ISOFilesLocation=(parent_dir+ directoryISOfiles)
PythonFilesLocation=(parent_dir+ directoryPython)
ConfigFilesLocation=(parent_dir+ directoryConfigs)
LogFilesLocation=(parent_dir+ directoryLogs)
TextFilesLocation=(parent_dir+ directoryText)
RemoteDesktopFilesLocation=(parent_dir+ directoryRemoteDesktop)
WebFilesLocation=(parent_dir+ directoryWeb)




#moving files -------------------------------------------

print('Moving documents')
for file in filename:
    if os.path.splitext(file)[1] in documents:
        if(path.exists(DocumentsLocation)):
            shutil.move(file,DocumentsLocation)
        else:
            print('Directory not found')

time.sleep(0.1)

print('Moving pictures')

for file in filename:
    if os.path.splitext(file)[1] in pictures:
        if(path.exists(PictureLocations)):
            shutil.move(file,PictureLocations)
        else:
            print('Directory not found')

time.sleep(0.1)

print('Moving videos')

for file in filename:
    if os.path.splitext(file)[1] in movies:
        if(path.exists(MovieLocation)):
            shutil.move(file,MovieLocation)
        else:
            print('Directory not found')

time.sleep(0.1)

print('Moving installation files')

for file in filename:
    if os.path.splitext(file)[1] in installers:
        if(path.exists(SetupFilesLocation)):
            shutil.move(file,SetupFilesLocation)
        else:
            print('Directory not found')

time.sleep(0.1)
            
print('Moving compressed files')

for file in filename:
    if os.path.splitext(file)[1] in compressedFiles:
        if(path.exists(CompressedFilesLocation)):
            shutil.move(file,CompressedFilesLocation)
        else:
            print('Directory not found')


time.sleep(0.1)
            
print('Moving photoshop-files')

for file in filename:
    if os.path.splitext(file)[1] in photoshop:
        if(path.exists(PhotoshopFilesLocation)):
            shutil.move(file,PhotoshopFilesLocation)
        else:
            print('Directory not found')


time.sleep(0.1)
            
print('Moving 3D-files')

for file in filename:
    if os.path.splitext(file)[1] in models:
        if(path.exists(ModelFilesLocation)):
            shutil.move(file,ModelFilesLocation)
        else:
            print('Directory not found')


time.sleep(0.1)
            
print('Moving Audio-files')

for file in filename:
    if os.path.splitext(file)[1] in sounds:
        if(path.exists(SoundFilesLocation)):
            shutil.move(file,SoundFilesLocation)
        else:
            print('Directory not found')


time.sleep(0.1)
            
print('Moving Torrent-files')

for file in filename:
    if os.path.splitext(file)[1] in torrents:
        if(path.exists(TorrentFilesLocation)):
            shutil.move(file,TorrentFilesLocation)
        else:
            print('Directory not found')


time.sleep(0.1)
            
print('Moving ISO-files')

for file in filename:
    if os.path.splitext(file)[1] in ISOfiles:
        if(path.exists(ISOFilesLocation)):
            shutil.move(file,ISOFilesLocation)
        else:
            print('Directory not found')


time.sleep(0.1)
            
print('Moving python-files')

for file in filename:
    if os.path.splitext(file)[1] in python:
        if(path.exists(PythonFilesLocation)):
            shutil.move(file,PythonFilesLocation)
        else:
            print('Directory not found')


time.sleep(0.1)
            
print('Moving config-files')

for file in filename:
    if os.path.splitext(file)[1] in configs:
        if(path.exists(ConfigFilesLocation)):
            shutil.move(file,ConfigFilesLocation)
        else:
            print('Directory not found')


time.sleep(0.1)
            
print('Moving Log-files')

for file in filename:
    if os.path.splitext(file)[1] in logs:
        if(path.exists(LogFilesLocation)):
            shutil.move(file,LogFilesLocation)
        else:
            print('Directory not found')


time.sleep(0.1)
            
print('Moving text-files')

for file in filename:
    if os.path.splitext(file)[1] in text:
        if(path.exists(TextFilesLocation)):
            shutil.move(file,TextFilesLocation)
        else:
            print('Directory not found')


time.sleep(0.1)
            
print('Moving RemoteDesktop-files')

for file in filename:
    if os.path.splitext(file)[1] in RemoteDesktop:
        if(path.exists(RemoteDesktopFilesLocation)):
            shutil.move(file,RemoteDesktopFilesLocation)
        else:
            print('Directory not found')


time.sleep(0.1)
            
print('Moving WEB-files')

for file in filename:
    if os.path.splitext(file)[1] in Web:
        if(path.exists(WebFilesLocation)):
            shutil.move(file,WebFilesLocation)
        else:
            print('Directory not found')




time.sleep(0.1)

print('Move complete!')

time.sleep(2)







#removing empty folders ----------------------------------

print('Deleting empty folders...')

emptyFolders = list()

for (dirpath, dirnames, filenames) in os.walk(parent_dir):
    if len(dirnames) == 0 and len(filenames) == 0 :
        emptyFolders.append(dirpath)

for element in emptyFolders:
    os.rmdir(element)


time.sleep(2)

print('Empty folders deleted!')
print('Sorting done!')

input("Press any key to continue...")