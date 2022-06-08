# Mission to Mars Web App

## Project Overview 
The purpose of this project is to automate a web browser to visit different websites to extract data about the Mission to Mars. 
Data will be stored in a no SQL data base (Mongo DB), and will be rendered in a web app using Flask. 

## Software 

- Python 3.7
- splitner 0.14.0
- webdriver-manager 3.3.0
- Flask-PyMongo 2.3.0
- BeautifulSoup
- html5lib

## Scraping Mars Data 

HTML PAGE:
<img width="619" alt="Screen Shot 2022-06-08 at 2 32 34 PM" src="https://user-images.githubusercontent.com/98793962/172696086-04a0723e-ddc4-415d-9593-9ab19ace97d4.png">

"Scrape New Data" button will load the lates news, images, and facts about mars. 
News titles and summaries are scraped from [NASA Mars Exploration Program News](https://data-class-mars.s3.amazonaws.com/Mars/index.html). The featured images from the [Jet Propulsion Laboratory's Space Images](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html). Mars hemisphere imagesfrom [Astropedia](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars). Mars facts table were scraped from [Galaxy Facts](https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html). Scraping code was ran in [scraping.py](https://github.com/schoolboycamel/mars_miss/blob/main/scraping.py).

[app.py](https://github.com/schoolboycamel/mars_miss/blob/main/app.py) allows us to extract the data and store it in Mongo DB.  A data base called "mars_app" was created, inside it, a collection called "mars" was also created, where all of our data is stored. 
Below we can see a screenshot confirming the data base and the collection.
commands used:
- "show dbs" which shows all data bases
- "use mars_app" which selects that specific db 
- "show collections" which shows all of the collections within that scpecific data base 
- "db.mars.find()" which shows all of the data within the collection 

![Screen Shot 2022-06-08 at 2 58 10 PM](https://user-images.githubusercontent.com/98793962/172698756-5ee7d3cc-f2c4-43b0-b4cd-206e2ea6718e.png)

## Updating Web App

Three different bootstrap features where used.

first two:

- Along with Jumbotron, I inserted a background image, positioned it center, and  covered the whole jumbotron header 
- H1 color was changed to white.

code:

![Screen Shot 2022-06-08 at 3 23 09 PM](https://user-images.githubusercontent.com/98793962/172700667-a048e11d-9403-4b06-8d09-fbcac3f58db2.png)

Product:

<img width="944" alt="image" src="https://user-images.githubusercontent.com/98793962/172702180-197d0024-75fc-4caa-a65e-a10f97f6f98d.png">


Third bootstrap feature:

- <div class="col-md-3"> allows the hemispehere images to be displayed side by side on desktop browsers.
  
<img width="1316" alt="Screen Shot 2022-06-08 at 3 20 47 PM" src="https://user-images.githubusercontent.com/98793962/172701104-391ded81-0cdc-467f-9894-1c6ae3bfbac2.png">
  
 ## Mobile responsivness
  
  <img width="619" alt="Screen Shot 2022-06-08 at 2 33 03 PM" src="https://user-images.githubusercontent.com/98793962/172701524-8ee6372c-e43f-40d9-85ad-b825498e0edf.png">

  


