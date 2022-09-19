import os
from PIL import Image, ImageFilter, ImageOps

rtName = ""

Config = {
	"directoryString" : f'C:/Users/jeffrey.moody/Documents/GitHub/etb/src/bla/art/bulk/',
	"directoryDestinationString" : f'C:/Users/jeffrey.moody/Documents/GitHub/etb/src/bla/art/bulk/RT',
	"testFile" : f"art/bulk/{rtName}"

}
		

def SetWorkingDirectory():
	# FileNnames List
	fileNameList = []

	# Set the working directory to the current python file directory
	os.chdir(os.path.abspath(os.path.dirname(__file__)))

	print("Working Directory: ", f"{os.getcwd()}")

	# Get list fo files and  directories
	print("List of files and directories: ", f"{os.listdir()}")

	# Get list of files only
	for f in os.listdir():
		if '.py' not in f:
			if '.' in f: 
				print(f)
				

	return fileNameList

if __name__ == '__main__':

	# Set the working directory to the current python file directory

	SetWorkingDirectory()

	detail = False


	if detail == True:
		# Config stuff

		Config = {
			"directoryString" : f'C:/Users/jeffrey.moody/Documents/GitHub/etb/src/bla/art/bulk/',
			"directoryDestinationString" : f'C:/Users/jeffrey.moody/Documents/GitHub/etb/src/bla/art/bulk/RT',
			"testFile" : r"art/bulk/akh-260-island-poole-300x225.png"

		}

		directoryString = f'C:/Users/jeffrey.moody/Documents/GitHub/etb/src/bla/art/bulk/'
		directoryDestinationString = f'C:/Users/jeffrey.moody/Documents/GitHub/etb/src/bla/art/bulk/RT'

		testFile = r"art/bulk/akh-260-island-poole-300x225.png"


		#pull the path from the parsed url
		fileNamePath = Config["testFile"]

		#get the substring after the last / character
		fileName = fileNamePath[fileNamePath.rfind('/')+1:]


		# The filename and extension
		fileNameExtension = os.path.splitext(fileName)

		#Splitting off the extension abbreviation from the filetype
		fileNameAndExtensionArray = fileNameExtension[1].split('.')

		#Create three main permutations to help train the engine on the land art images

		# Base Image
		# Set the save directory and filename
		FilePath = os.path.normpath(Config["testFile"])
		
		im = Image.open(FilePath)

		# Convert to RBG color mode to ensure other operations are successful. 
		im = im.convert("RGB")

		# Flipped Image
		imt = im
		imt = imt.transpose(Image.FLIP_LEFT_RIGHT)

		# Grayscale image
		imr = im
		imr = imr.convert('L')

		# Flipped Grayscale Image
		imtr = imt.convert('L')

		# Autocontrast - Color
		imac = im
		imac = ImageOps.autocontrast(im, cutoff=5, ignore=5)

		# Autocontrast - Grayscale
		imacg = imac.convert('L')

		# Flipper autocontratsed images
		imact = imac.transpose(Image.FLIP_LEFT_RIGHT)
		imacgt = imacg.transpose(Image.FLIP_LEFT_RIGHT)

		# Add Results
		resultingImages = [im, imt, imr, imtr, imac, imacg, imact, imacgt]
		resultingFilenamePrefixes = ["im", "imt", "imr", "imtr", "imac", "imacg", "imact", "imacgt"]
		
		displayResults = False

		# Display the results.
		if displayResults == True:
			for outImage in resultingImages:
				outImage.show()

		i = 0
		# Save the results.
		for saveImage in resultingImages:

			# Set the filename prefix to organize based on opperations executed
			filePrefix = resultingFilenamePrefixes[i]

			# set the file prefix so we can sort these images later if needed
			modifiedFileName = f"{filePrefix}_{fileNameExtension[0]}"

			# the file type should be determined automaticlly based on the input string. If needed this can be set manually.
			destinationString = f'art/bulk/RT/{modifiedFileName}.{fileNameAndExtensionArray[1]}'

			print("Filename: ", destinationString)

			# normalize and set the os directory path from our created string.
			DestinationPath = os.path.normpath(destinationString)

			# Save the image to the designated folder
			saveImage.save(DestinationPath)

			# Positively increment for the filename list
			i += 1


