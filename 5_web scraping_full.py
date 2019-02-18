##Web scraper of imdb pages
##This gets the first 250 entries from the list of 2018 movies sorted by number of votes
##each page has 50 entries so the code loops over the first 5 pages of this list
##to increase/decrease the number of movies to return update the pages list

import requests
import bs4 as bs
import re
from pandas import DataFrame
from time import sleep

url = 'http://www.imdb.com/search/title?release_date=2018&sort=num_votes,desc&start='
pages = list(range(1, 202, 50))
pages = [str(i) for i in pages]


#create empty lists to be filled
titles = []
revenues = []
ratings = []


##start of the for loop
for p in pages:
    pg = url + p
    
    #get url
    response = requests.get(pg)
    
    #parse with beautiful soup
    imdb_soup = bs.BeautifulSoup(response.text)
    
    #get the list of containers
    movie_containers = imdb_soup.find_all('div', class_ = 'lister-item-content')

    #fill lists with 
    for container in movie_containers:
        titles.append(container.h3.a.text)
        revenues.append(container.find_all("span")[-1].text)
        ratings.append(container.find("div", class_ = "inline-block ratings-imdb-rating").strong.text)

    #this just forces the loop to wait 5 seconds before scraping the next page
    #it's always a good idea to add a sleep call when you scrape multiple pages,
    #you don't want to overload their server and crash the page 
    sleep(5)
    
##end of for loop
###---------------------------------------------------------
    

    
###----------------------------------------------------------    
##now we can do our formatting
#format ratings as numeric
ratings = [float(i) for i in ratings]

#format revenues
revenues = [None if "$" not in rev else rev for rev in revenues]
revenues = [float(re.sub("[M$]", "", rev)) if rev is not None else rev for rev in revenues]
  


imdb_df = DataFrame({"Movie":titles,
                        "Revenues":revenues,
                        "Ratings":ratings})
    
imdb_df


#define a function to plot the movies by a variable.  
def plot_movies(df, x = "Ratings"):
    df2 = df.sort_values(by = x)
    return df2[-20:].plot.barh(x = "Movie", 
            y = x, 
            rot = 0, 
            color = "blue")    

#call the above function.  
plot_movies(imdb_df, "Ratings")
plot_movies(imdb_df, "Revenues")
plot_movies(imdb_df.dropna(), "Revenues")

##scatter plot with a lowess line (locally weighted regression line)
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure() #this is just because seaborn will add plots on top of each other...
sns.regplot(x = imdb_df["Ratings"], y = imdb_df["Revenues"], lowess = True)