###########################################################################################################
###########################################################################################################
# File: main
# Description:
###########################################################################################################
###########################################################################################################
from DuplicateFileFinder import findDuplicates
from FileOrganizer import organizeFiles

###########################################################################################################
# Name: main execution entry point
# Parameters:
###########################################################################################################
if __name__ == '__main__':
    # The Path of the directory to be sorted
    # path 			= '/Volumes/D1-WDBLACK5TB/Pictures'
    pathConsol 	= '/Volumes/D1-WDBLACK5TB/Consolidation'
    pathDest    = '/Volumes/D1-WDBLACK5TB/BitBucket'

    findDuplicates( pathConsol )
    organizeFiles( pathConsol, pathDest )


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