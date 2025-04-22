# A python module for system testing

# Import all classes from main source code
from Movies_Actors import Movies 
from Movies_Actors import MoviesList
from Movies_Actors import Actors
from Movies_Actors import ActorsList


#  movie object named ‘007’ with all the details required for a movie
movies_007 = Movies("1005", "007", "2000", "Action", "5/5/2000")

#  statement to call the movie object method to get all the details of the movie object “007”.
movies_007.describe_movie()

#  movie list object named ‘actions’ that contains ‘007’ object in the object’s collection
actions = MoviesList("")
actions.find_movie()

# actor object named ‘JamesBond’ with all the details required for an actor in the class.
JamesBond = Actors("James", "Bond", "Male", "4/3/1976")
JamesBond.describe_actor()

# actor list object named ‘all_actors’ that contains ‘JamesBond’ object in the object’s collection
all_actors = ActorsList("")

#  A statement to call the actor list object method to get the details of the actor James Bond
all_actors.find_actor()

# statement to call the actor list object method to remove the details of the actor James Bond from the collection
all_actors.remove_actor()

# statement to call the actor list object method to get the number of objects in its collection.
all_actors.number_of_actors()
