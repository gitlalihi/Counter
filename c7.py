# Python program that creates a 'Counter' for a list of items and converts it to a list of unique items with their counts.
from collections import Counter

def main():
    items=[]
    num=int(input("Enter your lists:"))
    for x in range(num):
       ele=input("Enter your elements:")
       items.append(ele)
    print("Your List is:",items) 
    item_counter = Counter(items)
    
    unique_items_with_counts = list(item_counter.items())
    
    print("Original List:", items)
    print("Counter:", item_counter)
    print("Unique Items with Counts:", unique_items_with_counts)

if __name__ == "__main__":
    main()