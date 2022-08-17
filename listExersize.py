# """
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
# """
from cmath import exp


month = ["January", "February", "March", "April", "May"]
expense = [2200, 2200, 2300, 2600, 2100,2190]
January = 2200
February = 2350
March = 2600
April = 2130
May = 2190
# 1. In Feb, how many dollars you spent extra compare to January?
print("the dollars you spent extra in feb compare to jan is:", February - January)
# 2. Find out your total expense in first quarter (first three months) of the year.
print("The total expense in first quarter is: ", January+February+March)
# 3. Find out if you spent exactly 2000 dollars in any month
print(2000 in expense)
# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
month.append("June")
expense.append(1980)
print(month)
print(expense)
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expense[2] = expense[2]-200
print(expense)
# __________________________________________
# __________________________________________
# __________________________________________
heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
print(len(heros))
# 2. Add 'black panther' at the end of this list
heros.append("black panther")
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
heros.insert(3, "black panther")
print(heros.pop(-1))
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros.remove(heros[1])
heros.remove(heros[1])
heros.insert(1, "Doctor strange")
print(heros)
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
print()
heros.__dir__
print(dir(heros))
heros.sort(reverse=False)
print(heros)
heros.sort(reverse=True)
print(heros)