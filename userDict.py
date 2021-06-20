import json
from difflib import get_close_matches
import os
import sys
data = json.load(open('data.json','r'))

#Ask for a word from user
#Give defintion of that word
#if its wrong ask if the mean a close word
def defintion(words):
   words = words.lower()
   if userInput == '':
      print("Please try again.")
      os.execl(sys.executable, sys.executable, *sys.argv)#restarts from the beginning
      

   if words in data:
      print(words)
      return data[words]
   elif len(get_close_matches(words, data.keys())) > 0:
      answer =   input('Did mean %s instead: For yes type y and no type n: ' % get_close_matches(words, data.keys())[0])
      
      if answer.lower() == 'y':
         return data[get_close_matches(words, data.keys())[0]]
      elif answer.lower() == 'n':
         print("Word doesn't exist in Dictanary. Please try again")
         os.execl(sys.executable, sys.executable, *sys.argv)#restarts from the beginning
      else:
         quit("Exiting program")




userInput = input('Please enter a word for the defintion: ')

output = defintion(userInput)
if type(output) == list:
   for defintion in output:
      print(defintion)
else:
   print(output)
