############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
# ANSWER:
  # 1) the for loop assigns numbers to beginning from 1 until 19. Not 20 as in range(a,b), b is not included. Therefore, 20 will never be assigned to i
  # 2) the if block checks if the value of i is equal to 20 and if it is, "You got it" is printed
  # 3) the statement is never printed when the code is run is because 20 is never assigned to i
# SOLUTION:
  # def my_function():
  #   for i in range(1, 21):
  #     if i == 20:
  #       print("You got it")
  # my_function()
# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# ANSWER:
  #1) We get the occational IndexError because when randint assigns 6 to dice_num and the element at 6th index it tried to access using disc_imgs[dice_num]. there is no element is 6th index. Even though the list has 6 elements their indices lie within [0,5] hence the occasional error
# SOLUTION:
  # from random import randint
  # dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
  # dice_num = randint(0, 5)
  # print(dice_imgs[dice_num])
# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

# Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# ANSWER:
  # Nothing gets printed when 1994 is entered is because 1994 is not included in either of the cases.
# SOLUTION:
  # year = int(input("What's your year of birth?"))
  # if year > 1980 and year <= 1994:
  #   print("You are a millenial.")
  # elif year > 1994:
  #   print("You are a Gen Z.")
# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# ANSWER:
  # 1) The input is not typecasted to 'int'
  # 2) The print statement in not indented to be included in the if block
  # 3) The string to printed is not made a f-string
# SOLUTION:
  # age = int(input("How old are you?"))
  # if age > 18:
  #   print(f"You can drive at age {age}.")
# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# ANSWER:
  #1) The word_per_page uses '==' instead of the assignment operator '='. Therefore, the input is never assigned to the variable and the product soted in total_words is always zero
  #2) We can use a print statement after each variable assignment to print the variables value to check what is causing the problem
# SOLUTION:
  # pages = 0
  # word_per_page = 0
  # pages = int(input("Number of pages: "))
  # print(f"No of pages= {pages}")
  # word_per_page = int(input("Number of words per page: "))
  # print(f"No of words per page= {word_per_page}")
  # total_words = pages * word_per_page
  # print(total_words)
# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
# ANSWER:
  #1) the 'b_list.append(new_item)' is not indented. Therefore, it only gets executed after the for loop and only once. Hence, only appending the last value of new_item which is the last element of a_list multiplied by 2.
# SOLUTION:
  # def mutate(a_list):
  #   b_list = []
  #   for item in a_list:
  #     new_item = item * 2
  #     b_list.append(new_item)
  #   print(b_list)
  
  # mutate([1,2,3,5,8,13])
# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------



