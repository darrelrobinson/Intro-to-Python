###Introduction to Python - Nackademin
## Session 5 - Getting data from web
## Based on AtBS Chapter 11 and a cool blog post:
## https://www.dataquest.io/blog/web-scraping-beautifulsoup/
import requests
import bs4 as bs #the beautiful soup module is the go-to module for parsing web data
#it turns the pile of web code that gets read into python with the requests.get call
#into something more manageable for which it is easier to extract the data that we want

#here is the webpage we are going to scrape, let's view it in our browser first and get a handle on it
url = 'http://www.imdb.com/search/title?release_date=2018&sort=num_votes,desc&page=1'


#the requests.get call pulls in the source code
response = requests.get(url)
print(response.text[:500])

#and beautifulsoup parses it so that it is easier to find elements in the code
imdb_soup = bs.BeautifulSoup(response.text)
#not that it is any easier to read for me
imdb_soup
type(imdb_soup)


#Let's go back to the page and start finding the pieces that we want using the inspector
#divs are containers, looking at the page we see that there is a div for each movie
movie_containers = imdb_soup.find_all('div', class_ = 'lister-item-content')
print(type(movie_containers))
print(len(movie_containers))

#now we can look at the container and its contents, there is one for each movie in the page
movie_containers[0]
movie_containers[1]

#can access different containers within the movie container
movie_containers[0].div


#the header for the div container
movie_containers[0].h3

#now we're getting close to the title
movie_containers[0].h3.a

#beautiful soup makes this easy, there is a text method
movie_containers[0].h3.a.text

#now, let's get some other information, the gross revenue and the rating
movie_containers[0].find_all("span")
movie_containers[0].find_all("span")[-1].text

#rating is a little clearer, there is a class to find
movie_containers[0].find("div", class_ = "inline-block ratings-imdb-rating").strong.text


#now, let's loop over all of the entries in movie containers to pull out the title, rating, and gross revenue
len(movie_containers)

#create some empty lists to store our data
titles = []
revenues = []
ratings = []

#then a normal for loop over our list of movie_containers
for container in movie_containers:
    titles.append(container.h3.a.text)
    revenues.append(container.find_all("span")[-1].text)
    ratings.append(container.find("div", class_ = "inline-block ratings-imdb-rating").strong.text)


titles
revenues
ratings

#format ratings as numeric
#we'll use a list comprehension to loop over ratings and coerce to float format
ratings = [float(i) for i in ratings]
ratings


#now let's fix our revenues, drop the ones that do not have a revenue
#how do we know which to remove? those that don't start with $ and end with M
revenues
revenues = [None if "$" not in rev else rev for rev in revenues]

#now we've changed all the non-revenue input to blank spaces
revenues


#next step is to convert the revenue data to numeric.
#I'll use a regular expression to find the $ and M in the string.
#regular expressions (regex) can be used by importing the re module
#it is a very powerful method of handling strings, but it is far from
#clear what the meaning of them are if you haven't worked much with them. 
#There is a brief introduction to regex in Automate the Boring Stuff, chapter 7
import re

#let's look at the third element of revenues as an example of what's happening here
revenues[2]
#we'll call an expression to replace M or $ with a "", to remove them in other words
re.sub("[M$]", "", revenues[2])
#the code gets rid of the M and $, but it is still formatted as text

#wrap a float() function around the whole thing to convert to numeric format
float(re.sub("[M$]", "", revenues[2]))

#now, apply this code to the entire list of revenues with a list comprehension
revenues = [float(re.sub("[M$]", "", rev)) if rev is not None else rev for rev in revenues]
revenues

 


##------------------------------------------------------------------------
#Finally, to do some visualization and simple statistical analysis, 
#we can put these lists into a dataframe
import pandas as pd
imdb_df = pd.DataFrame({"Movie":titles,
                        "Revenue":revenues,
                        "Ratings":ratings})
    
imdb_df


##some visualizations
imdb_df.plot(kind = "barh")


#let's look at the top-20
imdb_df2 = imdb_df.sort_values(by = "Ratings")
imdb_df2[-20:].plot.barh(x = "Movie", 
        y = "Ratings", 
        rot = 0, 
        color = "blue")


#let's look at the top-20 by revenues
imdb_df2 = imdb_df.sort_values(by = "Revenue")
imdb_df2[-20:].plot.barh(x = "Movie", 
        y = "Revenue", 
        rot = 0, 
        color = "blue")
#not very nice with all the missing values, we'll fix this below...

#but now that we've copy and pasted our code, we should write a function
def plot_movies(df, x = "Ratings"):
    df2 = df.sort_values(by = x)
    return df2[-20:].plot.barh(x = "Movie", 
            y = x, 
            rot = 0, 
            color = "blue")    

#let's use our function now instead...
plot_movies(imdb_df, "Ratings")
plot_movies(imdb_df, "Revenue")
plot_movies(imdb_df.dropna(), "Revenue")



#Examine the relationship between two variables...
#scatterplot of ratings v revenues
imdb_df.plot.scatter(x = "Ratings", y = "Revenue")

#add a lowess line to the plot, the plot shows some obvious non-linearity
import seaborn as sns
sns.regplot(x = imdb_df["Ratings"], y = imdb_df["Revenue"], lowess = True)



