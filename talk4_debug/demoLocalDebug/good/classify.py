import os
from infolib import FileInfo

KB = 1024
MB = 1024 * KB

DIRECTORY = "./images"
SIZE_LIMIT = 0.1 * MB


def getFiles(
		directory: str = "."
	) -> list:
	"""Get a list of FileInfo objects from specified directory."""
	
	fullpath = os.path.abspath(directory)
	files = []
	for filename in os.listdir(fullpath):
		filename = fullpath + os.sep + filename
		file = FileInfo(filename)
		files.append(file)
	return files

def getTotalSize(
		files: list
	) -> int:
	"""Obtain total size of files in the list."""

	totalSize = 0
	for index, file in enumerate(files):
		totalSize += file.size
	return totalSize

def filterBySize(
		files: list,
		maxSize: int = 2**40  # 1 TB
	) -> tuple:
	"""Filter a list of files based on their size.
	
	Returns a tuple of 2 lists with included and excluded files.
	"""
	
	included = []
	excluded = []
	for file in files:
		if file.size <= maxSize:
			included.append(file)
		else:
			excluded.append(file)
	return (included, excluded)

def exportCSV(
		files: list,
		csvFile: str = "output.csv"
	) -> None:
	"""Export CSV from list of files."""
	
	csvHeaders = "basename\tsize\tdatetime\n"
	csvData = [
			f"{file.basename}\t{file.size}\t{file.format_datetime()}\n"
			for file in files
	]

	# write data to output file
	print(f"Writing '{csvFile}'...")
	with open("csv" + os.sep + csvFile, "w") as output:
		output.write(csvHeaders)
		output.writelines(csvData)
	
	# print summary
	print(f"{len(files)} files.")
	totalMB = getTotalSize(files) / MB
	print(f"{totalMB:0.2} MB in files")

if __name__ == "__main__":
	images = getFiles(DIRECTORY)
	small, large = filterBySize(images, maxSize=SIZE_LIMIT)
	exportCSV(small, csvFile="small.csv")
	exportCSV(large, csvFile="large.csv")

