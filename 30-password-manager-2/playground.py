# # try except
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key" : "value"}
#     # print(a_dictionary["sdfsdf"])
#
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_mesage:
#     print(f"The key {error_mesage} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file closed")
#
# # rise own exceptions
# height = float(input("height: "))
# weight = int(input("weight: "))
#
# if height > 3:
#     raise ValueError("human height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)


# TODO: Catch the exception and make sure the code runs without crashing.
fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    try:
        fruit = fruits[index]

    except IndexError:
        print("fruit pie")
    else:
        print(fruit + " pie")

# 🚨 Do not change the code below
make_pie(4)

facebook_posts = [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass


print(total_likes)