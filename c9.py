# python program to find the Jaccard similarity coefficient between two lists using 'Counter' objects.
from collections import Counter

def jaccard_similarity(list1,list2):
    counter1=Counter(list1)
    counter2=Counter(list2)
    intersection_count=sum((counter1 & counter2).values())
    union_count=sum((counter1 | counter2).values())
    jaccard_coefficient=intersection_count/union_count
    return jaccard_coefficient

if __name__=='__main__':
    
    list1=[]
    num=int(input("Enter your lists:"))
    for x in range(num):
       ele=input("Enter your elements:")
       list.append(ele)
    print("Your  First List is:",list) 

    list2=[]
    num=int(input("Enter your lists:"))
    for x in range(num):
       ele=input("Enter your elements:")
       list.append(ele)
    print("Your  Second List is:",list2) 
    
    
    print(" The Jaccard similarity between two lists is ",jaccard_similarity)

