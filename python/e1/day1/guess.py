#Author:wqh
age_of_oldboy = 56
count = 0



while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy :
        print("yes,you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger!")
    count = count + 1
else:
    print("you have tired 3 times,game exit")



