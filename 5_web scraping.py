## Session 5 - Getting data from web
## Based on a blog post
## https://www.dataquest.io/blog/web-scraping-beautifulsoup/
import requests
import bs4 as bs


url = 'http://www.imdb.com/search/title?release_date=2018&sort=num_votes,desc&page=1'


response = requests.get(url)
print(response.text[:500])

imdb_soup = bs.BeautifulSoup(response.text)
imdb_soup
type(imdb_soup)


#divs are containers, looking at the page we see that there is a div for each movie
movie_containers = imdb_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))

#now we can look at the container and its contents, there is one for each movie in the page
movie_containers[0]
movie_containers[1]

#can access different containers within the movie container
movie_containers[0].div

#links start with a, this pulls out the links that are in the container
movie_containers[0].a

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

titles = []
revenues = []
ratings = []

for container in movie_containers:
    titles.append(container.h3.a.text)
    revenues.append(container.find_all("span")[-1].text)
    ratings.append(container.find("div", class_ = "inline-block ratings-imdb-rating").strong.text)

titles
revenues
ratings

#format ratings as numeric
ratings_float = [float(i) for i in ratings]
ratings_float


#now let's fix our revenues, drop the ones that do not have a revenue
#how do we know which to remove? those that don't start with $ and end with M
revenues
revenues = [None if "$" not in rev else rev for rev in revenues]

#the above is the same as the below for loop



#now we've changed all the non-revenue input to blank spaces
revenues

#I'll use a regular expression to find the $ and M in the string
#regular expressions (regex) can be used with the re module
#it is a very powerful method of handling strings, but it is far from
#clear what the meaning of them are if you haven't worked much with them. 
#There is a brief introduction to regex in Automate the Boring Stuff, chapter 7
import re
re.sub("[M$]", "", revenues[2])

revenues = [float(re.sub("[M$]", "", rev)) if rev != None else rev for rev in revenues]
revenues

 


##------------------------------------------------------------------------
#Finally, to do some visualization and statistical analysis, 
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



