# ___________________________________________#
# Regular Expressions By Izhar Ul Haq aka Izhar Khan Khattak #
# ___________________________________________#
# Dated : 27/12/2022 | VUSH Batch 14 | Lahore, Pakistan

import re
print(re.__version__)

#Check if the string starts with "The" and ends with "Spain":
# ___________________________________________#
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
# ___________________________________________#

#Check if the string starts with "The" and ends with "Spain":
#izhar
text = "The rain in Spain"
x = re.search("^I am.*Spain$", text)
if x:
  print("YES! We have a match!")
else:
  print("No match")
# ___________________________________________#
txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)
# ___________________________________________#

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)
# ___________________________________________#
txt = "hello planet hemmo" # hemmo should be in answer too

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)
# ___________________________________________#
txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
# ___________________________________________#
txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
# ___________________________________________#
txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)
# ___________________________________________#
txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)
# ___________________________________________#
txt = "hello planet"
# txt = "helo planet" # here it will return the helo

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"
# ___________________________________________#
txt = "hello planet"
# txt = "helo planet" # will return nothing

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)
# ___________________________________________#
txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
# ___________________________________________#
# Regular Expressions By Izhar Ul Haq aka Izhar Khan Khattak #
# ___________________________________________#