import winsound

while True:
    x = int(input("enter a number greater than 0: "))
    if x <= 0:
        winsound.Beep(450,500)
        print("greater than zero, please")
        continue
    else:
        winsound.Beep(1000,500)
        print("correct, thanks")
        break
