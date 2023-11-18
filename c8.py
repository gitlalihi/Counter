#Python program that creates a 'Counter' for a list of words and removes all items with a count less than a certain value.
from collections import Counter

def main():
    list = []
    num=int(input("Enter your lists:"))
    for x in range(num):
       ele=input("Enter your elements:")
       list.append(ele)
    print("Your List is:",list) 
    color_counter = Counter(list)
    
    min_count = int(input("Enter your minimum count:"))
    filtered_counter = {word: count for word, count in color_counter.items() if count >= min_count}
    
    print("Original List:", list)
    print("Counter:", color_counter)
    print(f"Items with Count >= {min_count}:", filtered_counter)

if __name__ == "__main__":
    main()