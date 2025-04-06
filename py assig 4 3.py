total = 0


for i in range(5):
    mark = int(input(f"Enter mark {i+1}: "))
    total = total + mark

# Calculate average
average = total / 5

# Grade evaluation based on average
if average >= 90 and average <= 100:
    print("A+")
elif average >= 80 and average < 90:
    print("A")
elif average >= 70 and average < 80:
    print("B")
elif average >= 60 and average < 70:
    print("C")
elif average < 60:
    print("Fail")
