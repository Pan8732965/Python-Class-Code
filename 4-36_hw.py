# 1 

# value = float(input("please enter a value："))
for number in range(1,101):
    if number % 13 == 0:
        print(number)
    
#4
inputValue = float(input("Pls enter your balance："))
if inputValue < 520001:
    FinalBalance = inputValue * 0.5
    print("Your final balance：",FinalBalance)
elif inputValue < 1170000 & inputValue > 520001:
    FinalBalance = inputValue * 0.12
    print("Your final balance：",FinalBalance)
elif inputValue < 2350000 & inputValue > 1170001:
    FinalBalance = inputValue * 0.2
    print("Your final balance：",FinalBalance)
elif inputValue < 4400000 & inputValue > 2350001:
    FinalBalance = inputValue * 0.3
    print("Your final balance：",FinalBalance)
elif inputValue >= 4400001:
    FinalBalance = inputValue * 0.4
    print("Your final balance：",FinalBalance)