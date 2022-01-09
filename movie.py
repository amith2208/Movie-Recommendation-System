import pandas as pd
import re

movies=pd.read_csv("Dataset/movies.csv")
ratings=pd.read_csv("Dataset/ratings.csv")
print("List of Movies")
print(movies.head())
print("***************************************************************************************************************************************")
print("Movie Ratings")
print(ratings.head())
print("***************************************************************************************************************************************")

final_data=pd.merge(ratings,movies,on='movieId')
print("List Of Movies Along With Ratings")
print(final_data.head())
print("****************************************************************************************************************************************")

print("Mean Rating Value by all Users")
print(final_data.groupby('title')['rating'].mean().sort_values(ascending=False).head())
print("****************************************************************************************************************************************")
print("Movie with Number Of Users Voted")
print(final_data.groupby('title')['rating'].count().sort_values(ascending=False).head())
print("***************************************************************************************************************************************")


print("List of MOVIES with Number of users voted and mean rating values")
movie_ratings=pd.DataFrame(final_data.groupby('title')['rating'].mean())
movie_ratings['no_of_ratings']=pd.DataFrame(final_data.groupby('title')['rating'].count())
print(movie_ratings.head())
print("****************************************************************************************************************************************")


movie_match=final_data.pivot_table(index='userId',columns='title',values='rating')
print("Matrix with UserId and ratings along with movie title")
print(movie_match.sort_values('userId',ascending=False).head(10))
print("Above List with Descending number of Users voted")
print(movie_ratings.sort_values('no_of_ratings',ascending=False).head(10))
print("****************************************************************************************************************************************")

def get_movie(name):
    if name in movie_match:
        movie_user_ratings=movie_match[name]
    else:
        name1='.*'+name+'.*'
        for Name in movie_match:
            if(re.match(name1,Name)):
                print('name -->',name)
                print('name -->',Name)
                movie_user_ratings=movie_match[Name]
                name=Name
                break
        else:
            print(" No match found in the list, Please try a different movie name")
            exit()

    print(name,"Movie Ratings")
    print(movie_user_ratings.head())
    print("************************************************************************************************************************************")

    similar_movie=movie_match.corrwith(movie_user_ratings)
    
    print("Movie with Its CORRELATION Values")
    corr_movie=pd.DataFrame(similar_movie,columns=['Correlation'])
    corr_movie.dropna(inplace=True)
    print(corr_movie.head())
    print("*************************************************************************************************************************************")


    corr_movie.sort_values('Correlation',ascending=False).head(10)
    corr_movie=corr_movie.join(movie_ratings['no_of_ratings'])
    corr_movie.head()
    print(name," Movie Similar to it are :-----")
    print(corr_movie[corr_movie['no_of_ratings']>100].sort_values('Correlation',ascending=False).head(10))
    print("***************************************************************************************************************************************")

print("===========================================================================================================================================")
print()
print('Enter a movie name')
name=str(input())
get_movie(name)

mean_ratings=movie_ratings['rating'].mean()
minimum_votes=movie_ratings['no_of_ratings'].quantile(0.75)

def imdb_rating(movie_ratings,m=minimum_votes,c=mean_ratings):
    v=movie_ratings['no_of_ratings']
    r=movie_ratings['rating']
    return ((v/v+m)*r)+((m/v+m)*c)


def top_movie():
    mean_ratings=movie_ratings['rating'].mean()
    print(" Mean rating Value : ",mean_ratings)

    minimum_votes=movie_ratings['no_of_ratings'].quantile(0.75)
    print(" Minimum Votes : ",minimum_votes)

    top_movies=movie_ratings.copy().loc[movie_ratings['no_of_ratings']>=minimum_votes]

    top_movies['imdb_rating']=top_movies.apply(imdb_rating,axis=1)
    top_movies=top_movies.sort_values('imdb_rating',ascending=False)
    print("The list of top 10 movies :")
    print(top_movies.head(10))
top_movie()
