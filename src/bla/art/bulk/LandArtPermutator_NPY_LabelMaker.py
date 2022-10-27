from matplotlib import image
from matplotlib import pyplot

from PIL import Image

import os	


file = os.listdir()[0]

# import the image using PIL

def SingleImagePIL(file):
	fimage = Image.open(file)
	return fimage

# Load an image as a pixel array
def SingleImageNPY(file):
	data = image.imread(file)
	return data

def LoadImagesFromDirectory(printResults):

	loadedImages = list()
	fileNames = list()

	for filename in os.listdir():

		# We are theoretically only able to load images with this function.
		# To brute force this we are just erroring when we try to load something the module doesn't like.
		# not the best but should be effective enough.

		try:
			# Load the image
			imgData = SingleImageNPY(file=filename)

			# Store the image
			loadedImages.append(imgData)
			
			# Store the filename
			fileNames.append(filename)

			if printResults == True:
				print('> loaded %s %s', (filename, imgData.shape))

		except:
			
			if printResults == True:
				print('> failed to load %s %s', (filename))

	# We return a list of filenames along with images
	return [fileNames, loadedImages]


def GetFileNameLabels(filename):
	# Headers: [filename, edition, number, type, artist]
	# Expected row format:[[filename, edition, number, type, artist]]

	# here we are removing the modification prefic and the filenames for tag generation
	modRemoved = filename
	modRemoved = modRemoved.split('.')
	fileString = modRemoved
	
	fileLabels = fileString[0].split('-')

	if len(fileLabels)-1 <= 3 :
		# Insert a blank record for th eartist if there isn't one
		# This isn't the best way, but works in a pinch with the given data
		fileLabels.insert(3, 'None')

	fileLabels.insert(0, filename)

	return fileLabels

def SaveCSV(labels):

	csvRaw = open('labels.csv', 'w')

	csvRaw.writelines("filename, edition, number, type, artist, dimensions\n")

	for label in labels:
		
		csvRecord = f"{label[0]}, {label[1]}, {label[2]}, {label[3]}, {label[4]}, {label[5]}\n"
		
		print(csvRecord)

		csvRaw.writelines(csvRecord)

	csvRaw.close()

	return csvRaw


if __name__ == '__main__':

	loadedImages = LoadImagesFromDirectory(printResults=False)

	finalizedLabels = []

	for imageLabel in loadedImages[0]:

		label = GetFileNameLabels(filename=imageLabel)

		finalizedLabels.append(label)


	SaveCSV(labels=finalizedLabels)

