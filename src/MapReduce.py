import csv
import os
from collections import defaultdict

def mapper(list1, filename):#maps key, value pairs into a list of lists
  with open(filename, 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    rows = [[row[0], int(row[1])] for row in reader if row]#converts the numeric values from strings to integers
  for row in rows:
    list1.append(row)#appends rows list to list1

def shuffleSort(res):#shuffles and sorts key, value pairs
  for name in res:
    res.sort()

def makeDict(res):#creates a dictionary with lists(arrays) of values for each unique key
  res1 = defaultdict(list)
  for i, j in res: 
    res1[i].append(j)#appends keys and values to dictionary
  dict1 = dict(res1)
  return dict1

def reduceStep(res, list5):#reduces(finds average)users of each type of social media
  newDict = makeDict(res)
  list3 = []
  list4 = []
  
  for key,value in newDict.items():
    avg = sum(value)/len(value)#finds the average of the lists for each key in the dictionary
    list3.append(round(avg, 2))#adds the rounded average to list3

  for keys in newDict:
    list4.append(keys)#adds the keys to list4

  for i in range(len(list4)):
    list5.append(list4[i])#adds the key to list5
    list5.append(list3[i])#adds the value to list5

if __name__ == "__main__":

  outfile = open("outfile.txt", "w")

  # create list of files to be read from
  file_list = []
  year = 2015
  for numyear in range(6):
    filename = str(year) + ".csv"
    file_list.append(filename)
    year += 1

  list1 = []
  for file in file_list:
    mapper(list1, file)
  res = list(tuple(sub) for sub in list1)#creates a list of tuples with key, value pairs
  outfile.write('*' *20)
  outfile.write(f'\nMapper:\n\n{res}\n')
  outfile.write("\n")
  outfile.write('*' *20)

  print('*'*20)
  print(f'Mapper:\n\n{res}\n')
  print('*'*20)

  shuffleSort(res)

  outfile.write("\n")
  outfile.write('*' *20)
  outfile.write('\nShuffle/Sort:\n\n')
  for name in res:
    outfile.write(f'{str(name)}\n')
  outfile.write("\n")
  outfile.write('*' *20)
  outfile.write("\n")

  print('*'*20)
  print('Shuffle/Sort:\n')
  for name in res:
    print(name)
  print('*'*20)

  x = []

  reduceStep(res, x)

  it = iter(x)
  finalDict = dict(zip(it, it))#iterates and creates a dictionary(key, value pair) for every 2 items in the list

  outfile.write('*' *20)
  outfile.write('\nAverage users for each type of Social Media:\n\n')
  for key,value in finalDict.items():
    outfile.write(f'{key}: {value}\n')
  outfile.write('*' *20)

  print('*'*20)
  print('Average users for each type of Social Media:\n')
  for key,value in finalDict.items():
    print(f'{key}: {value}')
  print('*'*20)

  outfile.close()
