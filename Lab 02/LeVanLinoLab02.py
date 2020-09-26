# *** LAB 02: PYTHON PRACTICE ***

# OBJECTIVE 1: Get accustomed to Python syntax and formatting.
# OBJECTIVE 2: Review concepts of logic, strings, conditionals, and operators.

# NOTE #1: Return statements are used as placeholders below. Change them as necessary.
# NOTE #2: Look up formatting/syntax if you are not sure how it looks in Python.

# EXERCISE 1: Five More Minutes
def moreSleep (weekday, vacation):
  """
  The parameter (input) weekday is True if it is a weekday.
  The parameter vacation is True if we are on vacation.
  We sleep in if it is not a weekday or if we are on vacation.
  Return True if we sleep in.
  """
  return not weekday or vacation

print("moreSleep:")
print(moreSleep(False, False)) # True
print(moreSleep(True, False)) # False
print(moreSleep(False, True)) # True
print("")

# EXERCISE 2: Barrelled Over
def jumpOver (bar1, bar2):
  """
  We have two gorillas, Donkey Kong and King Kong, and
  the parameters bar1 and bar2 indicate if each released a barrell.
  Mario is in trouble if they both release a barrell or
  if neither of them did (meaning they will attack).
  Return True if Mario is in trouble and needs to jump.
  """
  return bar1 == bar2

print("jumpOver:")
print(jumpOver(True, True)) # True
print(jumpOver(False, False)) # True
print(jumpOver(True, False)) # False
print("")

# EXERCISE 3: That Sums it Up
def doubleSum (x, y):
  """
  Given two int values, return their sum.
  Unless the two values are the same, then return double their sum.
  """
  return (x+y)*2 if x==y else x+y

# def doubleSum (x, y):
#   if(x==y):
#     return (x+y)*2
#   else:
#     return x+y
#   return (x+y)*2 if x==y else x+y

print("doubleSum:")
print(doubleSum(1, 2)) # 3
print(doubleSum(3, 2)) # 5
print(doubleSum(2, 2)) # 8
print("")

# EXERCISE 4: Wish Granted
def askWish (yapping, time):
  """
  Iago is Jafar's loud parrot. The yapping parameter is True if Iago is talking.
  The time parameter indicates the current hour in the range from 1 - 24.
  Return True if Iago is yapping before 6 or after 21 so Aladdin can wish for him to stop talking.
  """
  return False if not yapping else (False if 6<=time<=22 else True)

# def askWish (yapping, time):
#   if(not yapping):
#     return False
#   else:
#     if 21>=time>=6:
#       return False
#     else:
#       return True
#   return False if not yapping else (False if 6<time<22 else True)

print("askWish:")
print(askWish(True, 4)) # True
print(askWish(True, 7)) # False
print(askWish(False, 6)) # False
print("")

# EXERCISE 5: No Pun In-10-ded
def is10 (x, y):
  """
  Given 2 ints, x & y, return True if one of them is 10 or if their sum is 10.
  """
  return x==10 or y==10 or x+y == 10

print("is10:")
print(is10(9, 10)) # True
print(is10(9, 9)) # False
print(is10(1, 9)) # True
print("")

# EXERCISE 6: Almost One Pun-dred
def almostHund (n):
  """
  Given an int n, return True if it is within 10 of 100 or if it is within 10 of 200.
  Note: abs(num) computes the absolute value of a number.
  """
  return abs(100-n)<=10 or abs(200-n)<=10

print("almostHund:")
print(almostHund(93)) # True
print(almostHund(90)) # True
print(almostHund(89)) # False
print(almostHund(197)) # True
print(almostHund(211)) # False
print("")

# EXERCISE 7: Abs-olutely
def diff21 (n):
  """
  Given an int n, return the absolute difference between n and 21,
  except return double the absolute difference if n is over 21.
  """
  return abs(21-n)*2 if n>21 else abs(21-n)

# def diff21 (n):
#   if(n>21):
#     return abs(21-n)
#   else:
#     return abs(21-n)*2

print("diff21:")
print(diff21(19)) # 2
print(diff21(10)) # 11
print(diff21(21)) # 0
print(diff21(24)) # 6
print("")

# EXERCISE 8: Stringing You Along
def dupStr (str, n):
  """
  Given a string, str, and an integer, n, return a larger string that is n copies of the input string.
  Hint: Use a for loop & a variable which takes an empty string.
  """
  return str * n

# def dupStr (str, n):
#   final = ""
#
#   for i in range(0,n):
#       final+=str
#   return final

print("dupStr:")
print(dupStr('Hi', 2)) # HiHi
print(dupStr('Hi', 3)) # HiHiHi
print(dupStr('Hi', 1)) # Hi
print("")

# EXERCISE 9: Tag, You're it
def tagIt (tag, word):
  """
  HTML strings like "<i>Hurray</i>" allow for words to be typed in italic text.
  In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
  Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
  """
  return f"<{tag}>{word}</{tag}>"

print("tagIt:")
print(tagIt('i', 'Yay')) # <i>Yay</i>
print(tagIt('i', 'Hello')) # <i>Hello</i>
print(tagIt('cite', 'Yay')) # <cite>Yay</cite>
print("")

# EXERCISE 10: Avengers Assemble
def assembled (n, atTower):
  """
  Tony Stark is having a party. All the Avengers show up when there is between 50 and 100 guests inclusive.
  The parameter, n, represents the number of guests.
  If the party is held at Stark Tower, then there is no upper bound on the number of guests.
  Return True if all the Avengers will show up at the party.
  """
  return n>=50 if atTower else 100>=n>=50

# def assembled (n, atTower):
#   if(atTower):
#     return n>=50
#   else:
#     return 100>=n>=50

print("assembled:")
print(assembled(30, False)) # False
print(assembled(50, False)) # True
print(assembled(70, True)) # True
print(assembled(200, True)) # True
print(assembled(10, True)) # False
print("")

# EXERCISE 11: Save Hyrule?
def ganonDefeat (link, zelda):
  """
  Link & Zelda are in a battle with Ganondorf.
  The parameter link is the probability of his success with the sword in the range from 1 - 10
  while the parameter zelda is the probaility of her success with the bow & arrow.
  The likelihood of defeating Ganondorf is encoded as an int value where 0 = no, 1 = possibly, & 2 = yes.
  If either Link or Zelda have a success probability of 8 or more, the result is yes.
  However, if either one has a 3 or below, the result is no.
  In all other cases, the result is possibly.
  (If one has 8 or more and the other has 3 or below, the answer is also possibly.)
  """
  return 1 if max(link,zelda)>=8 and min(link,zelda)<=3 else (0 if min(link,zelda)<=3 else (2 if max(link,zelda)>=8 else 1))

# def ganonDefeat (link, zelda):
#   if(max(link,zelda)>=8 and min(link,zelda)<=3):
#     return 1
#   elif(min(link,zelda)<=3):
#    return 0
#   elif(max(link,zelda)>=8):
#    return 2
#   else:
#     return 1

print("ganonDefeat:")
print(ganonDefeat(5, 10)) # 2
print(ganonDefeat(5, 2)) # 0
print(ganonDefeat(5, 5)) # 1
print(ganonDefeat(8, 3)) # 1
print("")

# EXERCISE 12: How Alarming
def setAlarm (day, vacation):
  """
  Given a day of the week, encoded as 1 = Sunday, 2 = Monday, 3 = Tuesday, ... 7 = Sat,
  & a boolean indicating if we are on vacation, return a string of the form "7:00"
  indicating when the alarm clock should ring. On weekdays, the alarm should be "7:00";
  on the weekend, it should be "10:00". But if we are on vacation, then on weekdays
  it should be "10:00" & on weekends, it should be "off".
  """
  return ("10:00" if 6>=day>=2 else "off") if vacation else ("7:00" if 6>=day>=2 else "10:00")

# def setAlarm (day, vacation):
#     if(vacation):
#         if(6>=day>=2):
#             return "10:00"
#         else:
#             return "off"
#     else:
#         if(6>=day>=2):
#             return "7:00"
#         else:
#             return "10:00"

print("setAlarm:")
print(setAlarm(4, False)) # 7:00
print(setAlarm(1, False)) # 10:00
print(setAlarm(7, True)) # off
print("")
