# def movie_ticket_booking():
#     AVAILABLE_MOVIES = [
#     {"title": "Toy Story", "age": 6},
#     {"title": "Harry Potter and the Sorcerer's Stone", "age": 15},
#     {"title": "The Dark Knight", "age": 13},
#     {"title": "Titanic", "age": 18},
#     {"title": "The Matrix", "age": 18}
# ]

#     for i,movie_detail in enumerate(AVAILABLE_MOVIES):
#         print(f"{i+1}. {movie_detail["title"]} ({movie_detail["age"]}+)")


#     user_input = int(input("choose movie number: "))
#     user_age = int(input("Enter your age: "))

#     if AVAILABLE_MOVIES[user_input-1]["age"] > user_age:
#         print(f"Sorry requied age is {AVAILABLE_MOVIES[user_input-1]["age"]}+")
#     else:
#         while True:
#             try:
#                 ticket_no = int(input("Enter how many ticket you want to buy: "))
#             except ValueError:
#                 print("Enter valid number!")
            







# movie_ticket_booking()



movies ={
	1. ,("thelion king",10)
}

for key,movie_detail in (movies):
	print(f"{i+1}. {movie_detail["title"]} ({movie_detail["age"]}")

user_choice = int(input("Choose movie number: "))
user_age = int(input("Enter your age: "))

if movies[user_choice-1]["age"] > user_age:
	print(f"Requied age is {movies[user_choice-1]["age"]}")
	
else:
		tickets = int(input("Enter how many ticker you want to buy: "))
		if tickets <= 0:
			print("Enter valid ticket value!")
		else:
			print(f"{tickets} tickets booked! Thanks for coming")