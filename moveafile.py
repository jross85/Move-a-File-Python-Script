#moving files from my desktop to a
#specific folder on my desktop
import os
import shutil

#Be sure to be in the directory your python program is in before running

sourcePath = '/Path/To/Your/Source'
source = os.listdir(sourcePath)
destinationPath = '/Destination/You/Want/Your/File/Moved/To'


def scanAndMoveFiles():
    #check for file exstensions
    for files in source:
        if files.endswith('.png') or files.endswith('.gif') or files.endswith('.mp4') or files.endswith('JPG') or files.endswith('jpg') or files.endswith('.pdf'):
            #then move them
            shutil.move(os.path.join(sourcePath, files), os.path.join(destinationPath,files))



#call the method
scanAndMoveFiles()

#Just for confirmation that the program ran
print 'all your files have been moved'
