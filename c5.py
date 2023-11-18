#Python program that creates a counter of the words in a sentence and prints the words in ascending and descending order of their frequency.
from collections import Counter

def main():
    sentence = input("Enter your Sentence:")
    words = sentence.split()
    word_counter = Counter(words)
    print("Words in Ascending Order:")
    sorted_words_asc = sorted(word_counter.items(), key= get_count(),reverse=False)
    for word, count in sorted_words_asc:
        print(f"{word}: {count}")
    
    print("\n")
    
    
    print("Words in Descending Order:")
    sorted_words_desc = sorted(word_counter.items(), key=get_count(), reverse=True)
    for word, count in sorted_words_desc:
        print(f"{word}: {count}")

def get_count(item):
    return item[1]

if __name__ == "__main__":
    main()