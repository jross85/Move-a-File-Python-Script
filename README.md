# The Lazy Programmer's Tool to Moving Files Using Python
## Move Specific Files to a Specified Folder In under 10 Seconds

I wrote this script in 7 minutes because I was tired of manually moving all of my Android-related pictures and video files to a specified folder. The time I spent moving those files could have been time spent being productive.


Code Snippet:
```python
def scanAndMoveFiles():
    #check for file exstensions
  for files in source:
        if files.endswith('.png') or files.endswith('.gif') or files.endswith('.mp4')
        or files.endswith('JPG') or files.endswith('jpg') or files.endswith('.pdf'):
            #then move them
            shutil.move(os.path.join(sourcePath, files), os.path.join(destinationPath,files))

```

be sure to import os and import shutil as well.



*Credits to stackoverflow for the helpful tips on achieving this.*
