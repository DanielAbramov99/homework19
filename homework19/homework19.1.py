oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman",
                 "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth",
                   "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

oscar_winners.add("Emma Watson", )
print(f"after adding Emma Watson to the list:{oscar_winners}")
oscar_copy = oscar_winners.copy()
oscar_copy.remove("Meryl Streep")
print(f"after removing Meryl Streep from the list:{oscar_copy}")
oscar_copy.clear()
print(f"after clearing the set:{oscar_copy}")
common_actors = dark_knight_actors.intersection(titanic_actors)
print(f"the actors that played in both the titanic and the dark knight are:{common_actors} ")
common_actors2 = avengers_actors.intersection(iron_man_actors)
print(f"the actors that played in both the avengers and the iron man are:{common_actors2} ")
oscar_actors = actor_list.issubset(oscar_winners)
print(f"are all actors in this list won oscar:{oscar_actors}")
actor_avengers = actor_list.intersection(avengers_actors)
print(f"the actors from actors list that played in avengers are:{actor_avengers}")
actor_removed = movie_cast.pop()
print(f"the actor that been removed from the cast is {actor_removed}")
if "Matt Damon" in movie_cast:
    movie_cast.remove("Matt Damon")
print(f"after matt damon was removed{movie_cast}")
titanic_actors_no_oscar = titanic_actors.difference(oscar_winners)
print(f"the actors that played in titanic but didn't get an oscar are:{titanic_actors_no_oscar}")
no_intersect = dark_knight_actors.symmetric_difference(titanic_actors)
print(f"the actors that played only in one of the following films (dark knight or titanic) are:{no_intersect}")
oscar_winners.update({"Blanchett Cate", "Lewis-Day Daniel", })
print(f"after update:{oscar_winners}")
dark_titanic = dark_knight_actors.union(titanic_actors)
print(f"dark knight and titanic actors together:{dark_titanic}")
