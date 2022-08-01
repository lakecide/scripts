import os
from path import Path

sentence = "This is a common interview question"

char_frequency = {}

for chars in sentence:
    if chars in char_frequency:
        char_frequency[chars] += 1
    else:
        char_frequency[chars] = 1 

char_sorted = sorted(char_frequency.items(), 
                     key=lambda kv: kv[1] , 
                     reverse=True)
print(char_sorted[0])


directory = "test"
for files in os.listdir(directory):
    f = os.path.join(directory, files)
    rename = os.rename(f, f + ".exe")
   
    
  
    
    