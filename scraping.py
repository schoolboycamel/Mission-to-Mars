# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 

# Set up splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the Mars news site. 
url = 'https://redplanetscience.com/'
browser.visit(url)


# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# Convert the browser.html into a soup object 
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')


# Use the parent element to find the first <a> tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# Use the parent element to find the the paragraph text 
news_p = slide_elem.find('div', class_= 'article_teaser_body').get_text()
news_p


# ### Featured Images and change the code cell to "Markdown"

# visit the url 
url = 'https://spaceimages-mars.com/'
browser.visit(url)


# find and click the full image button 
#must make sure to look at devtool
full_image_elem = browser. find_by_tag('button')[1]
full_image_elem.click()


# Once the image is loaded wi will parse the resulting html with soup
html = browser.html
img_soup =soup(html, 'html.parser')


# find the relative image url 
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


#use the base url to create an absolute URL 
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# ### Mars Facts 

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# Convert DataFrame into HTML format 
df.to_html()


# Quit the automated browser. 
browser.quit()





