import os
from math import ceil
from random import randint


'''
    COMMENTS WILL SOON BE ADDED. 
    IF YOU WANT TO CONTRIBUTE THEN PLEASE FEEL FREE TO DO SO. 
'''

allFiles = os.walk('./').next()[2]
allFiles.remove('thanos.py')

totalFiles = len(allFiles)
halfCount = int(ceil(totalFiles / 2))

print("Thanos has Arrived!\n\n*** SNAP ***\n")


for i in range(halfCount):
    try:
        randomNum = randint(0, len(allFiles)-1)
        deleteFile = allFiles.pop(randomNum)
        os.remove(deleteFile)
    except:
        print('Bug encountered! {} {}'.format(randomNum, allFiles))
        
print("Thanos has killed {} out of {} files.".format(halfCount, totalFiles))
