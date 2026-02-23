#WAp to ask user to enter name of 3 fav movies & store them in a list & print the list

movies = []
movie1 = input("enter 1st fav movie: ")
movie2 = input("enter 2nd fav movie: ")
movie3 = input("enter 3rd fav movie: ")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)


#or other way to write ans of above question

movies =[]
movies.append(input("enter 1st fav movie: "))
movies.append(input("enter 2nd fav movie: "))
movies.append(input("enter 3rd fav movie: "))
print(movies)



#or other methods
movies =[]
mov = input("enter 1st fav movie: ")
movies.append(mov)
mov = input("enter 2nd fav movie: ")
movies.append(mov)
mov = input("enter 3rd fav movie: ")
movies.append(mov)
print(movies)