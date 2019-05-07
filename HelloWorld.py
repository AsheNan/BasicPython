# print ("Hello World!")
# name = "Nan"
# age = 26
# a = 3
# b = a
# print (id(a), id(b))

# a = input("name:")
#
# if a == "Alex":
#     print("He is the Boss!")
# elif a == "Eric":
#     print("hmm...")
# else :
#     print("We are friends!")

# Guess your lucky number
luckyNumber = 330
yourGuess = 0
guess_count = 0
# while True:
# while yourGuess != luckyNumber:
while yourGuess != luckyNumber and guess_count < 3:
    guess_count += 1
    yourGuess = eval(input("lucky number : "))
    if yourGuess > luckyNumber:
        print("smaller")
    elif yourGuess < luckyNumber:
        print("bigger")
    else:
        print("yeah!")
        # break

for i in range(3):
    print(i)


