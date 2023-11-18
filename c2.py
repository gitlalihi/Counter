#Python program that creates a 'Counter' from a list of elements and print the most common elements along with their counts.
from collections import Counter

list=[]
num=int(input("Enter your lists:"))
for x in range(num):
    ele=input("Enter your elements:")
    list.append(ele)
print("Your List is:",list)    
element_counter = Counter(list)

print("Most Common Elements:")
for element, count in element_counter.most_common():
    print(f"{element}: {count}")