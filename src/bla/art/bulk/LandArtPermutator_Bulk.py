import os, numpy
from PIL import Image, ImageFilter, ImageOps

rtName = ""

Config = {
	"directoryString" : f'C:/Users/jeffrey.moody/Documents/GitHub/etb/src/bla/art/bulk/',
	"directoryDestinationString" : f'C:/Users/jeffrey.moody/Documents/GitHub/etb/src/bla/art/bulk/RT',
	"testFile" : f"art/bulk/{rtName}"

}
		

def SetWorkingDirectory():

	# Set the working directory to the current python file directory
	os.chdir(os.path.abspath(os.path.dirname(__file__)))

	print("Working Directory: ", f"{os.getcwd()}")

	# Get list fo files and  directories
	# print("List of files and directories: ", f"{os.listdir()}")

	return [os.getcwd(), os.listdir()]

def GetFileList():
	fileNameList = []
	# Get list of files only
	for f in os.listdir():

		if '.py' not in f:

			if '.' in f:

				fileNameList.append(f) 

	print("Image count: ", len(fileNameList))

	return fileNameList

def CreateFileDirectoryList(_fileNameList):
	
	fileDirectoryList = []

	for f in _fileNameList:

		fileDirectoryList.append(f"{os.getcwd()}\\{f}")
		
	return fileDirectoryList

def OpenImageForProcessing(_fileDirectoryList):
	images = []

	# Iterate through the listed images and open them.
	for d in _fileDirectoryList:

		im = Image.open(d)

		# set the image mod to ensure we can perform needed operations
		im.convert("RGB")

		images.append(im)

	return images


# Dont use this one as it does not work. It is being kept here as there is some code for autocontrasts that need to be salvaged for further processing Retouched images.
def ProcessImages(_images, _fileNameList):

	processedImages = []
	processedFileNames = []

	resultingFilenamePrefixes = ["im", "imt", "imr", "imtr", "imac", "imacg", "imact", "imacgt"]

	i = 0

	# Iterate through the list of images performing the necessary operations on each
	# This is being done while updating our list of filenames to ensure we have an ordered and matched list.
	# Not the best solution, but the solution I know how to execute right now.
	for pI in _images:

		# Flipped Image
		imt = pI
		imt = imt.transpose(Image.FLIP_LEFT_RIGHT)
		processedImages.append(imt)
		processedFileNames.append(f"{resultingFilenamePrefixes[0]}_{_fileNameList[i]}")

		# Grayscale image
		imr = pI
		imr = imr.convert('L')
		processedImages.append(imr)
		processedFileNames.append(f"{resultingFilenamePrefixes[1]}_{_fileNameList[i]}")


		# Flipped Grayscale Image
		imtr = imt.convert('L')
		processedImages.append(imtr)
		processedFileNames.append(f"{resultingFilenamePrefixes[2]}_{_fileNameList[i]}")


		"""
		Commenting this out for now as it seems that some image modes fail with the listed operation
		Maybe on future iterations I can figure this out.

		# Autocontrast - Color
		imac = pI
		imac = ImageOps.autocontrast(pI, cutoff=5, ignore=5)
		processedImages.append(imac)
		processedFileNames.append(f"{resultingFilenamePrefixes[3]}_{_fileNameList[i]}")


		# Autocontrast - Grayscale
		imacg = imac.convert('L')
		processedImages.append(imacg)
		processedFileNames.append(f"{resultingFilenamePrefixes[4]}_{_fileNameList[i]}")


		# Flipper autocontratsed images
		imact = imac.transpose(Image.FLIP_LEFT_RIGHT)
		processedImages.append(imact)
		processedFileNames.append(f"{resultingFilenamePrefixes[5]}_{_fileNameList[i]}")

		imacgt = imacg.transpose(Image.FLIP_LEFT_RIGHT)
		processedImages.append(imacgt)
		processedFileNames.append(f"{resultingFilenamePrefixes[6]}_{_fileNameList[i]}")
		"""

		i += 1

		return [processedImages, processedFileNames]

def ProcessAndSaveImages(_images, _fileNameList):
	
	processedImages = []
	processedFileNames = []

	resultingFilenamePrefixes = ["im", "imt", "imr", "imtr", "imac", "imacg", "imact", "imacgt"]

	i = 0

	# Iterate through the list of images performing the necessary operations on each
	# This is being done while updating our list of filenames to ensure we have an ordered and matched list.
	# Not the best solution, but the solution I know how to execute right now.
	for f in _fileNameList:

		processedFileName = ""
		
		# Flipped Image
		imt = _images[i]
		imt = imt.transpose(Image.FLIP_LEFT_RIGHT)

		processedFileName = f"{resultingFilenamePrefixes[0]}_{_fileNameList[i]}"

		SaveImage(_imageName=processedFileName, _processedImage=imt)
		
		# Grayscale image
		imr = _images[i]
		imr = imr.convert('L')

		processedFileName = f"{resultingFilenamePrefixes[1]}_{_fileNameList[i]}"

		SaveImage(_imageName=processedFileName, _processedImage=imr)
		
		# Flipped Grayscale Image
		imtr = imt.convert('L')

		processedFileName = f"{resultingFilenamePrefixes[2]}_{_fileNameList[i]}"

		SaveImage(_imageName=processedFileName, _processedImage=imtr)

		i += 1


def SaveImage(_imageName, _processedImage ):
	# print(_destinationString)
	# print(_processedImagesLists[0], _processedImagesLists[1])

	# C:\Users\jeffrey.moody\Documents\GitHub\etb\src\bla\art\bulk\RT
	# <PIL.Image.Image image mode=RGBA size=300x246 at 0x25DB182AF10> im_5ed-430-plains-morrissey-300x246.png

	# Build destination strings and save images
	
	baseDestinationString = f"{os.getcwd()}\\RT"

	_processedImage.save(f"{baseDestinationString}\\{_imageName}")



if __name__ == '__main__':

	# Set the working directory to the current python file directory

	directory = SetWorkingDirectory()
	print(directory[0])
	fileList = GetFileList()

	sourceDirectoryList = CreateFileDirectoryList(_fileNameList=fileList)

	images = OpenImageForProcessing(_fileDirectoryList=sourceDirectoryList)

	ProcessAndSaveImages(_images=images, _fileNameList=fileList)