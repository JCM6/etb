import requests, json
import os

from bs4 import BeautifulSoup

from urllib.parse import urlparse



# Key parameters here are offset and posts_per_page
# Once we know the max we can query for the html that displays all land art resource links


# Obtain the html that will then be rendered to html.

def ObtainHtml(_url):

	response = requests.get(url=_url)

	jsonHtml = json.loads(response.text)

	html = jsonHtml['html']
	
	return html


# Plains Function
def ObtainPlainsHtml():

	url = "https://basiclandart.com/wp-admin/admin-ajax.php?id=&post_id=166&slug=plains&canonical_url=https%3A%2F%2Fbasiclandart.com%2Ftag%2Fplains%2F&posts_per_page=236&page=0&offset=0&post_type=post&repeater=default&seo_start_page=0&preloaded=false&preloaded_amount=0&tag=plains&order=DESC&orderby=date&action=alm_get_posts&query_type=standard"
	
	html = ObtainHtml(_url=url)
	
	return html

# Island Function
def ObtainIslandHtml():

	url = "https://basiclandart.com/wp-admin/admin-ajax.php?id=&post_id=167&slug=island&canonical_url=https%3A%2F%2Fbasiclandart.com%2Ftag%2Fisland%2F&posts_per_page=236&page=0&offset=0&post_type=post&repeater=default&seo_start_page=0&preloaded=false&preloaded_amount=0&tag=island&order=DESC&orderby=date&action=alm_get_posts&query_type=standard"
	
	html = ObtainHtml(_url=url)
	
	return html

# Swamp function
def ObtainSwampHtml():

	url = "https://basiclandart.com/wp-admin/admin-ajax.php?id=&post_id=168&slug=swamp&canonical_url=https%3A%2F%2Fbasiclandart.com%2Ftag%2Fswamp%2F&posts_per_page=236&page=0&offset=0&post_type=post&repeater=default&seo_start_page=1&preloaded=false&preloaded_amount=0&tag=swamp&order=DESC&orderby=date&action=alm_get_posts&query_type=standard"
	
	html = ObtainHtml(_url=url)
	
	return html

# Mountain Function
def ObtainMountainHtml():

	url = "https://basiclandart.com/wp-admin/admin-ajax.php?id=&post_id=169&slug=mountain&canonical_url=https%3A%2F%2Fbasiclandart.com%2Ftag%2Fmountain%2F&posts_per_page=237&page=0&offset=0&post_type=post&repeater=default&seo_start_page=1&preloaded=false&preloaded_amount=0&tag=mountain&order=DESC&orderby=date&action=alm_get_posts&query_type=standard"
	
	html = ObtainHtml(_url=url)
	
	return html

# Forest function
def ObtainForestHtml():

	url = "https://basiclandart.com/wp-admin/admin-ajax.php?id=&post_id=170&slug=forest&canonical_url=https%3A%2F%2Fbasiclandart.com%2Ftag%2Fforest%2F&posts_per_page=237&page=0&offset=0&post_type=post&repeater=default&seo_start_page=1&preloaded=false&preloaded_amount=0&tag=forest&order=DESC&orderby=date&action=alm_get_posts&query_type=standard"

	html = ObtainHtml(_url=url)
	
	return html
	

# Parse the html and generate a list of image links for the page.
def ParseAndExtractImageLinks(_html):

	soup = BeautifulSoup(_html)

	links = []

	for img in soup.find_all('img'):

		links.append(img['src'])
		
	return links

# Now that we have the links we need to stream the list of links to individual files
def DownloadImage(_link, _subFolder):
	
	#pull the path from the parsed url
	urlPath = urlparse(_link).path
	
	#get the substring after the last / character
	fileName = urlPath[urlPath.rfind('/')+1:]
	
	#call the url to stream the file
	image = requests.get(url=_link, stream=True)
	
	if image.status_code != 200:
	
		print('requestFailed')
		
	directoryString = f'C:/Users/jeffrey.moody/Documents/GitHub/etb/src/bla/art/{_subFolder}/{fileName}'
	
	directoryPath = os.path.normpath(directoryString)
	
	# Save the file to the art directory.
	saveFile = open(directoryPath, 'wb')

	saveFile.write(image.content)

	saveFile.close()
	
	return image
	

# Downloads all found images and returns a list of links we failed and succeeded downloading images from
def DownloadImages(_linkList, __subFolder):
	
	results = {"Successes":[], "Failures":[]}
	
	for link in _linkList:
	
		try:
		
			response = DownloadImage(_link=link, _subFolder=__subFolder)
			
			results["Successes"].append(link)
			
		except Exception as ex:
		
			results['Failures'].append({str(ex):{f"Response Status: {response.status_code}":link}})
			
			
	results = json.dumps(results, indent=4)
	
	return results


# Encapsulates the functions for downloading all forest images available
def DownloadSourceImages():

	# Here we establish which functions to iterate through
	# Right now we are relying on set urls for pulling images from the source. Not a great solution, but it works for now. 
	# One for each land type [Plains, Island, Swamp, Mountain, Forest]
	
	# htmlToObtain = [ObtainSwampHtml(), ObtainForestHtml()]
	
	htmlToObtain = [ObtainIslandHtml(), ObtainPlainsHtml(), ObtainMountainHtml()]
	
	for html in htmlToObtain:
		
		extractedRefs = ParseAndExtractImageLinks(_html=html)

		downloadResults = DownloadImages(_linkList=extractedRefs, __subFolder="bulk")

		print(downloadResults)

	

if __name__ == '__main__':

	DownloadSourceImages()

