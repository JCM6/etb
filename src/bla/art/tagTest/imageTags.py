from PIL import Image
from PIL.ExifTags import TAGS

imagetest = "znr-280-forest-x-259x300.png"
imagetest = "C:\\Users\\jeffrey.moody\\Documents\\GitHub\\etb\\src\\bla\\art\\tagTest\\znr-280-forest-x-259x300.png"
im = Image.open(imagetest)

metadata_basic = {
	"filename":im.filename,
	"size":im.size,
	"height":im.height,
	"width":im.width,
	"format":im.format,
	"mode":im.mode,
	# it is possible to extract animation datae , but we are going to ignore that for now
}

for label, value in metadata_basic.items():
	print(f"{label:25}: {value}")


# extracting EXIF data:

exifData = im.getexif()

    
for tagId in exifData:
    # get the human readable tag, but we could get the internal reference id
    tag = TAGS.get(tagId, tagId)

    data = exifData.get(tagId)

    if isinstance(data, bytes):
        data = data.decode()

    print(f"{tag:25}: {data}")