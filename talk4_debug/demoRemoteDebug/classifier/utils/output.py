import os
from .constants import KB, MB, WORKING_DIRECTORY

def getTotalSize(files: list) -> int:
	"""Obtain total size of files in the list."""

	totalSize = 0
	for index, file in enumerate(files):
		totalSize += file.size
	return totalSize

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
	with open(WORKING_DIRECTORY + os.sep + "csv" + os.sep + csvFile, "w") as output:
		output.write(csvHeaders)
		output.writelines(csvData)
	
	# print summary
	print(f"{len(files)} files.")
	totalMB = getTotalSize(files) / MB
	print(f"{totalMB:0.2} MB in files")

