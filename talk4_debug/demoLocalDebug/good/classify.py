import os
from utils import FileInfo
from utils.output import exportCSV
from utils.constants import MB


DIRECTORY = "images"
SIZE_LIMIT = 0.1 * MB


def getFiles(directory: str = ".") -> list:
	"""Get a list of FileInfo objects from specified directory."""
	
	fullpath = os.path.abspath(directory)
	files = []
	for filename in os.listdir(fullpath):
		filename = fullpath + os.sep + filename
		file = FileInfo(filename)
		files.append(file)
	return files

def classifyBySize(
		files: list,
		maxSize: int = 2**40  # 1 TB
	) -> tuple:
	"""Classify a list of files based on their size.
	
	Returns a tuple of 2 lists with small and big files.
	"""
	
	smallFiles = []
	bigFiles = []
	for file in files:
		if file.size <= maxSize:
			smallFiles.append(file)
		else:
			bigFiles.append(file)
	return (smallFiles, bigFiles)

if __name__ == "__main__":
	images = getFiles(DIRECTORY)
	small, large = classifyBySize(images, maxSize=SIZE_LIMIT)
	exportCSV(small, csvFile="small.csv")
	exportCSV(large, csvFile="large.csv")

