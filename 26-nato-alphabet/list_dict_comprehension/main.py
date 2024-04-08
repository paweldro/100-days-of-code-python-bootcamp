import random
import pandas

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Angela"
new_list_2 = [letter for letter in name]
print(new_list_2)

new_list_3 = [num * 2 for num in range(1, 5)]
print(new_list_3)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
new_list_4 = [name for name in names if len(name) < 5]
print(new_list_4)

new_list_5 = [name.upper() for name in names if len(name) > 5]
print(new_list_5)

numbers_2 = [1, 1, 2, 3, 5]
new_list_6 = [num * num for num in numbers_2]
print(new_list_6)

numbers_3 = "1,23,44,55,75,68,79,67"
list_of_strings = numbers_3.split(',')
numbers_4 = [int(x) for x in list_of_strings if int(x) % 2 == 0]
print(numbers_4)

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)
passed_students = {student: score for (student, score) in student_scores.items() if score > 50}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow"
sentence_result = {word: len(word) for word in sentence.split(" ")}
print(sentence_result)

weather_c = {'Monday': 4, 'Tuesday': 14, 'Wednesday': 15, 'Thursday': 14, 'Friday': 21, 'Saturday': 22, 'Sunday': 24}
weather_f = {day: (temp*9/5)+32 for (day, temp) in weather_c.items()}
print(weather_f)

student_dic = {"student": ["Angela", "James", "lily"], "score": [56, 76, 98]}
student_data_frame = pandas.DataFrame(student_dic)
print(student_data_frame)
print(" ")
for (index, row) in student_data_frame.iterrows():
    print(row.student)

