answer = input("What data type is the value 6.3? ")
score = 0

if answer == "float":
    print("You got it!")
    score += 1
elif answer == "integer":
    print("Integers can't have decimals.")
else:
    print("That is incorrect the correct answer is float")

answer = int(input("What does len(\"hi\") evaluate to? "))
if answer == 2:
    print("You got it!")
    score += 1
else:
    print("That is incorrect the correct answer is 2")

print(score)