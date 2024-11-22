from collections import deque
words = input("write a set of words ")
set_words = deque()
split_words = words.split()

 
for i in split_words:
      set_words.appendleft(i)
print("initial queue ", set_words)

print("the words with 'o' are: ")

for word in split_words:
    if 'o' in word:
     print(word)