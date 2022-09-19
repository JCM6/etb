from matplotlib import image
from matplotlib import pyplot

from PIL import Image

import os	


# import the image using PIL

file = os.listdir()[0]

fimage = Image.open(file)

# Load an image as a pixel array

data = image.imread(file)

print(data.dtype)
print(data.shape)

pyplot.imshow(data)
pyplot.show()