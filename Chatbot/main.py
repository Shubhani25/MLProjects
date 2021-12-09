from functions import *

home_bot = create_bot('Mike')

train_all_data(home_bot)

identity = input("State your identity please: ")

if identity == "Mark":
    print("Welcome, Mark. Happy to meet you.")

elif identity == 'Jane':
    print("Mark is busy right now. Welcome, I will accompany you.")

else:
    print("Your access is denied.")
    exit()

house_owner=[
    "Who is the owner?",
    "Mark Nicolas is the owner."
]

custom_train(home_bot, house_owner)

print("----Training Custom Data----")

if identity == 'Mark':
    city_born=[
        "Where was I born?",
        "Mark, you were born in Los Angeles."
    ]

    fav_book=[
        "What's you favourite book?",
        "Your favourite book is Power of a Man."
    ]

    fav_movie=[
        "What's you favourite movie?",
        "Your favourite movie is YJHD."
    ]

    fav_sports=[
        "What's you favourite sports?",
        "Your favourite sports is Cricket."
    ]

    custom_train(home_bot, city_born)
    custom_train(home_bot, fav_book)
    custom_train(home_bot, fav_movie)
    custom_train(home_bot, fav_sports)

start_chatbot(home_bot)
