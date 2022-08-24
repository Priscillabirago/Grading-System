name = input("Enter your name")
score = int(input("Enter examination score"))
Mark = int(score * 0.7)
mark = int(input("Enter 30 percent score"))
total = Mark + mark
if 100 >= total >= 80:
    grid = "A"
elif 80 > total >= 70:
    grid = "B"
elif 70 > total >= 60:
    grid = "C"
elif 60 > total >= 50:
    grid = "D"
elif 50 > total >= 40:
    grid = "E"
elif total < 40:
    grid = "F"
print("Hello " + name + ". You scored " + str(total) + ". Your grade is " + grid)






