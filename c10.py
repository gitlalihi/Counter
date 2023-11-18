#Python Program: Updating item counts using Counter objects
from collections import Counter

def update_counts(counter1, counter2):
    counter1.update(counter2)
    return counter1

def main():
    
    sentence1 = input("Enter your items")
    sentence2 = input("Enter another items")
    words1 = sentence1.split()
    words2 = sentence2.split()
    counter1 = Counter(words1)
    counter2 = Counter(words2)
    updated_counter = update_counts(counter1, counter2)
    print("Updated Counts:")
    for word, count in updated_counter.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
