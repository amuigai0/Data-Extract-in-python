from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = ''

#Connecting and grabbing page

uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, 'html.parser')

#find all containers

containers = page_soup.findAll('',{'' :''})

#creating and exporting extratct in a .csv file
filename = 'products.csv'
f =  open(filename, 'w')

headers = "\n"

f.write('')

#Loop to extract data wanted
for container in containers:
	
	brand_name = container.findAll('', {'':''})
	brand = brand_name[0].img['']

	title_name = container.findAll('', {'' : ''})
	product_name = title_name[0].text

	shipping_container = container.findAll('', {'' : ''})
	shipping = shipping_container[0].text.strip()

	print('Brand name:' + brand)
	print('Product:' + product_name)
	print('Shipping:' + shipping)

	#Writes extracted data in a .csv file
	f.write(brand + ',' +product_name.replace(",", "|") + ',' + shipping + '\n')

f.close()


