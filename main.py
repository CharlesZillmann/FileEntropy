###########################################################################################################
###########################################################################################################
# File: main
# Description:
###########################################################################################################
###########################################################################################################
from DuplicateFileFinder import findDuplicates
from FileOrganizer import organizeFiles
import sys

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
        # path 	 		= '/Volumes/D1-WDBLACK5TB/Pictures'
        #pathConsol = '/Volumes/D1-WDBLACK5TB/Consolidation'
        #pathDest = '/Volumes/D1-WDBLACK5TB/BitBucket'

        findDuplicates(pathConsol)
        organizeFiles(pathConsol, pathDest)
    else:
        print('Usage: python FileEntropy.py folder1 folder2')
        print('Where: folder1 is the path to the source folder to be consolidated and folder2 is the path to the destination folder that will contain the consolidated files.')
        print('Example: python FileEntropy.py /Volumes/D1-WDBLACK5TB/Consolidation /Volumes/D1-WDBLACK5TB/BitBucket')






# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         dups = {}
#         folders = sys.argv[1:]
#         for i in folders:
#             # Iterate the folders given
#             if os.path.exists(i):
#                 # Find the duplicated files and append them to the dups
#                 joinDicts(dups, findDup(i))
#             else:
#                 print('%s is not a valid path, please verify' % i)
#                 sys.exit()
#         printResults(dups)
#     else:
#         print('Usage: python dupFinder.py folder or python dupFinder.py folder1 folder2 folder3')


###########################################################################################################
###########################################################################################################
#                                             End File
###########################################################################################################
###########################################################################################################