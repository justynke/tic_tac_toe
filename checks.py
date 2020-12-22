scores = input().split()
corrects = 0
incorrects = 0

for score in scores:
    if score == "I":
        incorrects +=1
    elif score == "C" and incorrects < 3:
        corrects += 1

print(corrects)
print(incorrects)



if incorrects >= 3:
    print("Game over")
    print(corrects)
else:
    print("You won")
    print(corrects)
