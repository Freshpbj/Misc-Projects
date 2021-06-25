# takes 2 .txt files and combines them into 1 with all words seperated on a new line and removes all non-unique words

def pull(filename):
  text1 = open(filename, "r")
  return(text1.read())

def save_results(results):
  with open("results.txt", "w") as myfile:
    myfile.write('\n'.join(results))  # can change \n to , for a comma seperated list (.csv file)
    myfile.write('\n') #\n ends the line and starts a new one
    
text1 = pull(input('Name of first file:  '))
text2 = pull(input('Name of second file:  '))

new = text1 + text2
oldlist = new.split()
newlist = list(dict.fromkeys(oldlist))  #removes non-unique from list
newlist.sort()
save_results(newlist)
print('Success, file saved to results.txt')
