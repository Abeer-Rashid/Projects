
from pathlib import Path

import json

# import the random class to generate random numbers for Movie ID
import random

# Create the class Movies with getter and setter methods for Id, title, year, genre and release date
class Movies:

    def __init__(self, ID, title, year, genre, release_date):
        self.ID = ID
        self.title = title
        self.year = year
        self.genre = genre
        self.release_date = release_date
    
   # Method to retrieve the Movie ID 
    def get_ID(self):
        return self.ID
   
   # Method to set the Movie ID
    def set_ID(self, value):
        self.ID = value
   
   # Method to retrieve the Movie Title 
    def get_title(self):
        return self.title
    
   # Method to set the Movie Title 
    def set_title(self, value):
        self.title = value

   # Method to retrieve the movie year 
    def get_year(self):
        return self.year
    
   # Method to set the movie year 
    def set_year(self,value):
        self.year = value

   # Method to get Movie Genre 
    def get_genre(self):
        return self.genre
    
    # Method to set Movie Genre
    def set_genre(self, value):
        self.genre = value

   # Method to get Movie Release Date 
    def get_release_date(self):
        return self.release_date
    
    # Method to set Movie Release Date
    def set_release_date(self, value):
        self.release_date = value

    def describe_movie(self):
        print((f"\n{self.ID}--{self.title}({self.year}) is a {self.genre} movie released on {self.release_date}"))

  
# Movie Object
movies = Movies("", "", "", "", "")

# Dictionary to store the movie collection
location = Path(__file__).parent
with open(r"C:\Users\239357173_system_source_code.zip\data\MovieDictionary.json.txt", "r") as f:
    MovieDictionary = json.load(f)


     

class MoviesList:

    def __init__(self, MovieDictionary):
        self.MovieDictionary = MovieDictionary
        self.movie_details = {}
         
   #-------Add Movie Details: ID, Title, Year, Genre, Release Date------     
    def add_movie(self, movies):
        
        ID = movies.get_ID()
        ID = random.randint(1000,9999)
        self.movie_details["ID"] = ID
        print(ID)

        title = movies.get_title()
        title = input("Enter title here: ").title()
        self.movie_details["title"] = title
        print(title)

        year = movies.get_year()
        year = input("Enter year: ")
        self.movie_details["year"] = year
        print(year)

        genre = movies.get_genre()
        genre = input("Enter genre: ").title()
        self.movie_details["genre"] = genre
        print(genre)

        release_date = movies.get_release_date()
        release_date = input ("Enter release date: ")
        self.movie_details["release_date"] = release_date
        print(release_date)
        print(self.movie_details)
        MovieDictionary.update({title: self.movie_details})
        print(MovieDictionary)

        with open(r"C:\Users\239357173_system_source_code.zip\data\MovieDictionary.json.txt", "w") as f:
            json.dump(MovieDictionary, f)
        

   #----- Search Movie by Movie Title----- 
    def find_movie(self):
        
        for key in MovieDictionary:
            value = input("To search by name press 1:  ").lower()
            if value == "1":
                val = input("Enter Movie Title: ").title()
                print("\nMovie Details: ",MovieDictionary[val])
           
            else:
                print("\nNo Movie Found")
            break
   
   #-----Remove Movie-----     
    def remove_movie(self):
        title = input("Enter the name of the Movie to remove: ").title()
        del MovieDictionary[title]
        print(MovieDictionary)

   #-----To see how many Movies are in the Collection and view the Collection----- 
    def movie_collection(self):
        print(len(MovieDictionary))
        print(MovieDictionary)
        



class Actors:

    def __init__(self, firstname, surname, gender, dateofbirth):
        self.firstname = firstname
        self.surname = surname
        self.gender = gender
        self.dateofbirth = dateofbirth

   # Method to retrieve Actor First Name 
    def get_firstname(self):
        return self.firstname
    
   # Method to set Actor First Name 
    def set_firstname(self, value):
        self.firstname = value

   # Method to retieve Actor Surname 
    def get_surname(self):
        return self.surname
    
   # Method to set Actor Surname 
    def set_surname(self, value):
        self.surname = value

   # Method to retrieve Actors' Gender 
    def get_gender(self):
        return self.gender
    
   # Method to set Actors' Gender 
    def set_gender(self, value):
        self.gender = value

   # Method to retrieve Actors' Date of Birth 
    def get_dateofbirth(self):
        return self.dateofbirth
    
   # Method to set Actors' Date of Birth 
    def set_dateofbirth(self, value):
        self.dateofbirth = value

    def describe_actor(self):
        print(f"\n{self.firstname} {self.surname} is a {self.gender} actor born on {self.dateofbirth}")
    
# Actor object
actors = Actors("", "", "", "")

# Dictionary to store Actor Details
with open(r"C:\Users\hp\OneDrive\Documents\239357173_system_source_code.zip\data\ActorDictionary.json.txt", "r") as f:
    ActorDictionary = json.load(f)


class ActorsList:

    def __init__(self, ActorDictionary):
        self.ActorDictionary = ActorDictionary
        self.actor_details = {}

   #-----Add Actor: First Name, Surname, Gender, Date of Birth----- 
    def add_actor(self, actors):

        FirstName = actors.get_firstname()
        FirstName = input("Enter First Name: ").title()
        self.actor_details["First Name"] = FirstName

        SurName = actors.get_surname()
        SurName = input("Enter Surname: ").title()
        self.actor_details["Surname"] = SurName

        Gender = actors.get_gender()
        Gender = input("Enter Actor Gender: ").title()
        self.actor_details["Gender"] = Gender

        DateOfBirth = actors.get_dateofbirth()
        DateOfBirth = input("Enter Actor Date of Birth: ")
        self.actor_details["Date of Birth"] = DateOfBirth

        ActorDictionary.update({FirstName:self.actor_details})
        print(ActorDictionary)

        with open(r"C:\Users\hp\OneDrive\Documents\239357173_system_source_code.zip\data\ActorDictionary.json.txt", "w") as f:
            json.dump(ActorDictionary, f)


   #-----Find Actor by their First Name------ 
    def find_actor(self):
        for key in ActorDictionary:
            value = input("To search for an Actor based on their First Name, press 1: ")
            if value == "1":
                name = input("Enter Name: ").title()
                print("\nActor Details: ", ActorDictionary[name])
                
            break
            

   #-----Remove Actor from the Records----- 
    def remove_actor(self):
        name = input("Enter the First Name of the Actor to remove: ").title()   
        del ActorDictionary[name]
        print(ActorDictionary)

   #-----To see how many Actors are in the Records and to view the Records 
    def number_of_actors(self):
        print("The total number of Actors in the Records are: ", len(ActorDictionary))
        print(ActorDictionary)




def start():
    print("\nWelcome to the Movie Records Systems!\n")
    action = input("Would you like to access the Movie Record System? Type yes: ")
    action = action.upper()

    if action == "YES":
        return True
    
    else:
        return False
    
class Main:

    def __init__(self):
        
        movies_list = MoviesList("")
        
        actors_lists = ActorsList("")
        prompt = input("To Select the action you want to take type number.\n1 To Add a Movie to the collection \n2 To Search for a Movie in the collection \n3 To Remove a Movie from the collection \n4 To find out the number of Movies in the collection \n5 To Add an Actor to the record \n6 to Search an Actors details from the record \n7 To remove an actor from the record \n8 To see how many actors are in the record \nq to Quit\n\n")

        if prompt == "1":
            print("\nAdd Movie")
            movies_list.add_movie(movies)

        elif prompt == "2":
            print("\nFind Movie")
            movies_list.find_movie()

        elif prompt == "3":
            print("\nRemove Movie")
            movies_list.remove_movie()

        elif prompt == "4":
            print("\nThe number of movies in the collection are: ")
            movies_list.movie_collection()

        elif prompt == "5":
            print("\nAdd Actor to records")
            actors_lists.add_actor(actors)

        elif prompt == "6":
            print("\nSearch for Actor")
            actors_lists.find_actor()

        elif prompt == "7":
            print("\nRemove Actor from records")
            actors_lists.remove_actor()

        elif prompt == "8":
            print("\nThe number of actors in the collection: ")
            actors_lists.number_of_actors()

        elif prompt == "q":
            exit()
        
        else:
            print("\nYour choice is out of range. Try again. \n")
        
        
while start():
     Main()
     
 

   
