from PIL import Image, ImageFilter, ImageEnhance
import random
import math

# Notes and other details about data preparation and processing.
# Square shape 256×256 pixels.
# Rectangular images were resized to 256 pixels on their shortest side, then the middle 256×256 square was cropped from the image.
# Note: the network expects input images to have the shape 224×224, achieved via training augmentation.

# Data Preparation:
# A fixed size must be selected for input images, and all images must be resized to that shape. The most common type of pixel scaling involves centering pixel values per-channel, perhaps followed by some type of normalization.
# Train-Time Augmentation:
# required, most commonly involved resizing and cropping of input images, as well as modification of images such as shifts, flips and changes to colors.
# Test-Time Augmentation:
# Focused on systematic crops of the input images to ensure features present in the input images were detected.

#            #
# Operations #
#            #

# These functions will operate on images based on specific operations to ensure a degree of consistency in image manipulation.
# Resulting images will then be saved and added to the given set of incoming data.

# Set the size of the incoming image to a standard 256x256 px size.
# This will likely be reused in a couple other functions.
def Resizer256(image):
    
    outputSize = (256, 256)
    
    outputImage = image.resize(outputSize)

    return outputImage

# Random square crop and resize to produce varied image sample.
# 256x256 px image is expected here.
def Shifter(image, seed):

    width, height = image.size

    # left = int(seed)
    # top = height / int(seed) + 1
    # right = 126
    # bottom = 3 * height / int(seed) + 1

    left = seed
    top = 16 + seed + 10
    right = 64 + seed + 20
    bottom = 64 + seed + 80

    outputImage = image.crop((int(left), int(top), int(right), int(bottom)))

    outputImage = Resizer256(image=outputImage)

    return outputImage

# Performs a horizontal flip of the incoming image.
# 256x256 px image is expected here.
def Flipper(image):

    outputImage = image.transpose(Image.FLIP_LEFT_RIGHT)

    return outputImage

# Color Median 
# 256x256 px image is expected here.
def ColorMedian(image, filterSize):
    
    outputImage = image.filter(ImageFilter.MedianFilter(size=int(filterSize)))
        
    return outputImage

# Color Desturate
# This is parsed similalry to shifting the color wheel on a visual display. Not a 100% match with HueDesat but close enough.
# 256x256 px image is expected here.

def Desaturater(image):

    inImage = ImageEnhance.Color(image)

    outputImage = inImage.enhance(0.5)
    
    return outputImage

# Color Increase Vibrance
# 256x256 px image is expected here.
def BoostVibrancer(image):
    
    inImage = ImageEnhance.Color(image)

    outputImage = inImage.enhance(2)
    
    return outputImage

# Applies all three of the permutations to one image with a set of random values.
# 256x256 px image is expected here.
def Wildcard2(image):

    # Apply two
    operationList = [Shifter(image=image, seed=random.randint(16, 32)), Flipper(image=image ), ColorMedian(image=image, filterSize=9), Desaturater(image=image), BoostVibrancer(image=image)]

    imageStep1 = random.choice(operationList)

    operationList = [Shifter(image=imageStep1, seed=random.randint(16, 32)), Flipper(image=imageStep1 ), ColorMedian(image=imageStep1, filterSize=9), Desaturater(image=imageStep1), BoostVibrancer(image=imageStep1)]
    
    imageStep2 = random.choice(operationList)

    outputImage = imageStep2

    return outputImage

def SingleImageFlow(imageName, displayResults):

    fileDir = f'src\\scryfall_artcrops\\{imageName}.jpg'

    im = Image.open(fileDir)

    resized = Resizer256(image=im)

    shifted = Shifter(image=resized, seed=random.randint(16, 32))

    flipped = Flipper(image=resized )

    colorMedian = ColorMedian(image=resized, filterSize=9)

    desaturated = Desaturater(image=resized)

    vibranced = BoostVibrancer(image=resized)

    wild = Wildcard2(image=resized)

    if displayResults == True:

        print(im.format, im.size, im.mode)
        im.show()

        resized.show()
        
        shifted.show()
        
        flipped.show()
        
        colorMedian.show()
        
        desaturated.show()
        
        vibranced.show()
        
        wild.show()

    return

def TEST_FlowforSingleImage(imageName):

    SingleImageFlow(imageName=imageName, displayResults=True)

    
if __name__ == "__main__":

    TEST_FlowforSingleImage(imageName="8e862d50-8fa5-4b6e-af19-a161dc4c251d")