number_people = int(input("Home many people: "))
max_age = 0
position = -1
for i in range(number_people):
    age, gender = map(int, input().split())
    if gender == 1 and age > max_age:
        position, max_age = i+1, age
print(position)
4
