#Python program that creates a counter of the vowels in the word "Python Exercises".
from collections import Counter

word = "Python Exercises"
vowels = "aeiouAEIOU"  # List of vowels

vowel_ctr = Counter(c for c in word if c in vowels)

print("Vowel Counts:")
for vowel, count in vowel_ctr.items():
    print(f"{vowel}: {count}")