from sys import argv


#---------------------------
#      Functions
#---------------------------

def convertString(string):
  '''
    The convertion order is not random. This order allows that numbers passed as
    int remain int. If I had the float convertion first, inputs like '2' would be
    converted as 2.0
  '''
  try:
    return int(string)
  except:
    try:
      return float(string)
    except:
      return string


def avgNumber(numbers_array):
  return sum(numbers_array) / len(numbers_array)

#---------------------
#     Main Logic
#---------------------

numbers = []
words = []

for i in range(1, len(argv)): #Avoid the script name

  parsed = convertString(argv[i]) #convert to int or float all possible args

  if(isinstance(parsed, str)): #in case
    words.append(parsed)
  else:
    numbers.append(parsed)

print(avgNumber(numbers))
print(', '.join(words))