import os
from utils import FileInfo
from utils.output import exportCSV


DIRECTORY = "images"
WORKING_DIRECTORY = os.path.dirname(__file__)


def removeCSVFiles():
	csvDir = os.path.abspath(WORKING_DIRECTORY + os.sep  + "csv")
	csvFiles = [
			csvDir + os.sep + filename
			for filename in os.listdir(csvDir)
			if filename.endswith(".csv")
	]
	for filename in csvFiles:
		os.remove(filename)


def getFiles(directory: str = ".") -> list:
	"""Get a list of FileInfo objects from specified directory."""
	
	fullDirPath = WORKING_DIRECTORY + os.sep + directory
	files = []
	for filename in os.listdir(fullDirPath):
		filename = fullDirPath + os.sep + filename
		file = FileInfo(filename)
		files.append(file)
	return files

def classifyByFirstLetter(files: list) -> list:
	"""Classify a list of files based on the first letter of the name
	
	Returns a dictionary with key = firstLetter and value = filesStartingWithLetter
	"""
	
	classified = dict()
	firstLetters = set([
			file.basename[0]
			for file in files
	])
	for letter in firstLetters:
		included = []
		for file in files:
			if file.basename.startswith(letter):
				included.append(file)
		classified[letter] = included
	return classified

if __name__ == "__main__":
	allImages = getFiles(DIRECTORY)
	imagesByLetter = classifyByFirstLetter(allImages)
	removeCSVFiles()
	for letter, images in imagesByLetter.items():
		exportCSV(images, csvFile=f"{letter}.csv")
