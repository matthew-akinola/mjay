# importing libraries
from bs4 import BeautifulSoup
import requests

# instagram URL
URL = "https://www.instagram.com/{}/"

# parse function
def parse_data(s):
	
	# creating a dictionary
	data = {}
	
	# splitting the content
	# then taking the first part
	# s = s.split("-")
	
	# again splitting the content
	# s = s.split(" ")
	print(s)
	
	# returning the dictionary
	return data

# scrape function
def scrape_data(username):
	
	# getting the request from url
	r = requests.get(URL.format(username))
	
	# converting the text
	s = BeautifulSoup(r.text, "html.parser")
	
	# finding meta info
	meta = s.find("meta", property ="og:description")
	
	# calling parse method
	return parse_data(meta)

# main function
if __name__=="__main__":
	
	# user name
	username = "biden"
	
	# calling scrape function
	data = scrape_data(username)
	
	# printing the info
	print(data)
