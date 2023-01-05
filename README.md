# Web-scrapes---py
Web scrapes a website and stores the scraped data in an excel file

This script web scrapes a website and stores the scraped data in an excel file. It also downloads images from the website and saves them on the user's local machine.

To achieve this, the script imports the requests and BeautifulSoup modules to send HTTP requests and parse the HTML response, respectively. The xlsxwriter module is used to create an excel file and write the scraped data to it.

The script defines the download function to download an image from a given URL and save it to the user's local machine.

The get_url function generates a generator object that yields the URL of each page containing product data on the website. It does this by sending an HTTP request to each page and parsing the HTML response to extract the product data.

The array function is a generator that yields a tuple for each product containing the product data and the URL of the page containing the data. It does this by iterating over the generator object returned by the get_url function and sending an HTTP request to each page to retrieve the data.

The writer function takes in a generator as a parameter and writes the data yielded by the generator to an excel file. It does this by iterating over the generator object and writing each item in the tuple to a separate cell in the excel file.

Once the script is run, it will scrape the website, download the images, and save the data and images to the specified locations on the user's local machine.
