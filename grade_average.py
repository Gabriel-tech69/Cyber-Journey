grades = [85, 42, 76, 91, 53, 67]
total = 0
count = 0
for grade in grades:
    total = total + grade
    count = count + 1
average = total / count
print(f"Average grade: {average}")
