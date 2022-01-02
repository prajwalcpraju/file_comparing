import os
path="C:/Users/prajw/project/groups/"
file=os.listdir("C:/Users/prajw/project/groups/")

groups=[]
for i in file:
    if i.endswith(".txt"):
        with open(path+i,"r") as f:
            b=f.read()
            groups.append(b)
grp_name=['group1','group2','group3','group4','group5']

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

tk_words=[]
for i,items in enumerate(groups):
    t=word_tokenize(groups[i])
    tk_words.append(t)
    
fw_words=[]
for i,items in enumerate(tk_words):
    sw=stopwords.words('english')
    final_words=[word for word in items if word not in sw]
    final_words.sort()
    fw_words.append(final_words)
    
final_groups=list()
for i,items in enumerate(fw_words):
    fg= list()
    for item in fw_words[i]:
        if item not in fg:
            fg.append(item)
    final_groups.append(fg)

with open('sample.txt','r') as file:
        file_1=file.readlines()
tk_file= [phrase.split() for phrase in file_1]
sw=stopwords.words('english')
final_words=[word for word in tk_file[0] if word not in sw]
final_words.sort()

sample_file=list()
for item in final_words:
    if item not in sample_file:
        sample_file.append(item)

rating=[]
for i,items in enumerate(final_groups):
    a = set(final_groups[i])
    b = set(sample_file)
    similarity = float(len(a.intersection(b))*100)
    rating.append(similarity)

avg=(max(rating)-min(rating))/2
for i in range(5):
    if(rating[i]==max(rating)):
        print("maximum matching with "+grp_name[i])
    if(rating[i]>avg):
        print("Rating of "+grp_name[i]+" is : 3")
    else :
        if(rating[i]<avg and rating[i]>min(rating)):
            print("Rating of "+grp_name[i]+" is : 2")
        else:
            print("Rating of "+grp_name[i]+" is : 1")
    
