#####################################################################################################################
#####################################################################################################################
# File: main
# Description:
#####################################################################################################################
#####################################################################################################################
from DuplicateFileFinder import findDuplicates, printResults
from FileOrganizer import organizeFiles
from GUIInterface import showGUI, askSourceDirectory
import sys

#####################################################################################################################
# Code
#####################################################################################################################

###########################################################################################################
# Name: main execution entry point
# Parameters:
###########################################################################################################
if __name__ == '__main__':
    if len(sys.argv) > 2:
        print(f"Arguments count: {len(sys.argv)}")
        for i, arg in enumerate(sys.argv):
            print(f"Argument {i:>6}: {arg}")

        pathConsol = sys.argv[1]
        pathDest = sys.argv[2]
        print(f"Source Folder: {pathConsol}")
        print(f"Destination Folder: {pathDest}")

        # The Path of the directory to be sorted
        #pathConsol = '/Volumes/D1-WDBLACK5TB/Consolidation'
        #pathDest = '/Volumes/D1-WDBLACK5TB/BitBucket'
        showGUI()
        #print(f"Source Folder: {askSourceDirectory()}")

        #dups = findDuplicates(pathConsol)
        #printResults(dups)

        #organizeFiles(pathConsol, pathDest)
    else:
        print('Usage: python FileEntropy.py folder1 folder2')
        print('Where: folder1 is the path to the source folder to be consolidated and folder2 is the path to the destination folder that will contain the consolidated files.')
        print('Example: python FileEntropy.py /Volumes/D1-WDBLACK5TB/Consolidation /Volumes/D1-WDBLACK5TB/BitBucket')


#####################################################################################################################
#####################################################################################################################
#                                             End File
#####################################################################################################################
#####################################################################################################################