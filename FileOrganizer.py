###########################################################################################################
###########################################################################################################
# File: FileOrganizer
# Description:
###########################################################################################################
###########################################################################################################
from pathlib import Path
import os
import shutil



DIRECTORIES = {
	"HTML": [".html5", ".html", ".htm", ".xhtml"],

	"IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
			".heif", ".psd", ".ico", ".jpe", ".svg", ".ps"],
	"VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
			".qt", ".mpg", ".mpeg", ".3gp", ".m4v", ".m2ts"],
	"DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
				".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".dot",
				".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".numbers", ".key", ".ppt",
				".pptx", ".csv", ".sqlite"],
	"ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
				".dmg", ".rar", ".xar", ".zip", ".dat", ".pst", ".pcap", ".mdb", ".pkg"],
	"AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
			".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
	"PLAINTEXT": [".txt", ".in", ".out"],
	"PDF": [".pdf"],
	"CODE": [".py", ".java", ".h", ".c", ".cpp", ".eml", ".swift", ".json", ".vcproj", ".pl", ".o",
			 ".jsp", ".jsp", ".hx", ".hpp", ".hx"],
	"XML": [".xml", ".olk14Message", ".olk14Contact", ".olk14Event", ".olk14MsgAttach",
			".olk14CalAttach", ".olk14MsgSource"],
	"EXE": [".exe"],
	"SHELL": [".sh"]
}

FILE_FORMATS = {file_format: directory
				for directory, file_formats in DIRECTORIES.items()
				for file_format in file_formats}

###########################################################################################################
# Name: remove_empty_directories
# Parameters:
###########################################################################################################
def remove_empty_directories( thePath ):
	os.chdir(thePath)
	print(os.getcwd())

	for dir in os.scandir():
		try:
			os.rmdir(dir)
		except:
			pass

###########################################################################################################
# Name: consolidate_files_groups
# Parameters:
###########################################################################################################
def consolidate_files_groups( pathDest ):
	pathMISC = pathDest + '/MISC'
	myMiscFileCount = 0
	for entry in os.scandir():
		if entry.is_dir():
			continue
		file_path = Path(entry)
		file_format = file_path.suffix.lower()
		if file_format in FILE_FORMATS:
			directory_path = Path(pathDest + '/' + FILE_FORMATS[file_format])
			directory_path.mkdir(exist_ok=True)
			file_path.rename(directory_path.joinpath(file_path))
		else:
			myMiscFileCount =  myMiscFileCount + 1
			directory_path = Path(pathMISC + str(myMiscFileCount // 2000) )
			directory_path.mkdir(exist_ok=True)
			file_path.rename(directory_path.joinpath(file_path))

###########################################################################################################
# Name: consolidate_files_in_directory
# Parameters:
###########################################################################################################
def consolidate_files_in_directory( pathConsol, pathDest ):
	os.chdir(pathConsol)
	print(os.getcwd())

	for root,d_names,f_names in os.walk(pathConsol):
		for d in d_names:
			myPath = os.path.join(root, d)
			if os.path.isdir( myPath ):
				os.chdir(myPath)
				print(os.getcwd())
				consolidate_files_groups( pathDest )
				try:
					os.rmdir(myPath)
				except:
					pass

###########################################################################################################
# Name: organize_groups_into_subgroups
# Parameters:
###########################################################################################################
def organize_groups_into_subgroups( thePath ):
	# This populates a list with the filenames in the directory
	list_ = os.listdir(thePath)

	# Traverses every file
	for file_ in list_:
		name, ext = os.path.splitext(file_)
		print(name + ext)
		# Stores the extension type
		ext = ext[1:]
		# If it is directory, it forces the next iteration
		if ext == '':
			continue
		# If a directory with the name 'ext' exists, it moves the file to that directory
		if os.path.exists(thePath + '/' + ext):
			shutil.move(thePath + '/' + file_, thePath + '/' + ext + '/' + file_)
		# If the directory does not exist, it creates a new directory
		else:
			os.makedirs(thePath + '/' + ext)
			shutil.move(thePath + '/' + file_, thePath + '/' + ext + '/' + file_)

###########################################################################################################
# Name: getDirectoryPaths
# Parameters:
###########################################################################################################
def getDestDirectoryPaths( pathDest ):
	myPaths = []
	for key in DIRECTORIES.keys():
		myPaths.append(pathDest + "/" + key)
	myPaths.append(pathDest + "/MISC")
	return myPaths

###########################################################################################################
# Name: organizeSubgroups
# Parameters:
###########################################################################################################
def organizeSubgroups ( pathDest):
	directory_path = Path(pathDest)
	for myPath in getDestDirectoryPaths( pathDest ):
		directory_path.mkdir(exist_ok=True)
		organize_groups_into_subgroups( myPath )

###########################################################################################################
# Name: organizeFiles
# Parameters:
###########################################################################################################
def organizeFiles( pathConsol, pathDest ):
    path = os.getcwd()
    print(path)
    # /Users/mbp/Documents/my-project/python-snippets/notebook
    os.chdir(pathConsol)
    print(os.getcwd())

    directory_path = Path(pathDest)
    directory_path.mkdir(exist_ok=True)
    print(directory_path)

    consolidate_files_in_directory( pathConsol, pathDest )
    organizeSubgroups( pathDest )


###########################################################################################################
###########################################################################################################
#                                             End File
###########################################################################################################
###########################################################################################################

# directory_path = Path(pathMISC)
# directory_path.mkdir(exist_ok=True)
# organize_groups_into_subgroups(pathMISC)
#
# remove_empty_directories( pathConsol )