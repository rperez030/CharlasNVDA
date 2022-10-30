import os
from .constants import WORKING_DIRECTORY

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
	with open(WORKING_DIRECTORY + os.sep + "csv" + os.sep + csvFile, "w") as output:
		output.write(csvHeaders)
		output.writelines(csvData)
	
	# print summary
	print(f"{len(files)} files in '{csvFile}'...")

