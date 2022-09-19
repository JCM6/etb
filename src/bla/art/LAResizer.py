import os
from PIL  import Image


def ResizeImages(_path, _dirs):
	
	for file in _dirs:
		
								
		im = Image.open(_path + file)
		
		f = os.path.splitext(_path + file)
		print(f)
		imResize = im.resize((200, 200), Image.ANTIALIAS)

		imResize.save(f, 'JPEG')

if __name__ == '__main__':

	path = input("Enter the subfolder name: ")
	path = os.getcwd() + path
	print(path)
	dirs = os.listdir(path)

	ResizeImages(_path=path, _dirs=dirs)