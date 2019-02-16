#jaccard similarity using scikit in data science
#created by ikon beth
#DevCUyo100DaysOfCode

from sklearn.metrics import jaccard_similarity_score
#create two strings
str_1 = 'dogs chase cats'
str_2 =  'cats hate dogs'

#create set from strings
str1_set = set(str_1.split())
str2_set = set(str_2.split())

unq_wrds = str1_set.union(str2_set)

a = [1 if w in str1_set else 0 for w in unq_wrds]
b = [1 if w in str2_set else 0 for w in unq_wrds]

print (a,b)
print(jaccard_similarity_score(a,b))

input("Exit:")
