# Movie-Recommendation-System

Information-Retrieval-Project

<h2><strong>Introduction</strong></h2><br>
<p>An individual usually has a hard time finding a good movie according to their choice of genre,so we recommend them a list of movies over their ratings or genre or movies that are similar to the one requested and also the list of top rated movies.</p>
<p>We have used filtering techniques such as Content based filtering and Statistical based filtering to achieve our goal.</p>
<h2>Content Based Filtering</h2>
<p>Content-based Filtering is a technique that uses similarities in features to make decisions. This technique is often used in recommender systems, which are algorithms designed to advertise or recommend things to users based on knowledge accumulated about the user.</p>
<h2>Satistical Filtering</h2>
<p>Here we filter the data obtained by a weight variable i.e., Weighted Rating Which is calculated as ,
			(R*v+C*m)/(v+m)
Where,
v : number of votes for a movie 
m : minimum number of votes for a movie (75% in our case)
R : rating of the movie
C : mean rating of all the movies.
  </p>

