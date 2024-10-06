#Practice Problem
message = "Learning Python is fun and rewarding!"

#task 1 Extract the first 8 characters of the string
print(message[0:8])

#task 2 Extract the last 9 characters of the string.
print(message[-10:])

#task 3 Extract the word "Python" from the string.
print(message[9:15])

#task 4 Reverse the entire string.
print(message[::-1])

#task 5 Extract every third character from the string.
print(message[::3])
#[start:end:step] 

#Practice Problem2
sentence = "Mastering slicing in Python can be fun!"

#task 1 Extract the word "Mastering" from the string.
print(sentence[:10-1])
print(sentence[:9])

#task 2 Extract the last 4 characters of the string using a negative index.
print(sentence[-4:])

#task 3 Extract the phrase "slicing in Python" from the string.
print(sentence[9:27])

#task 4 Extract the entire string but skip every 2nd character.
print(sentence[::2])

#task 5 Reverse the words in the sentence 
# (hint: split the sentence into words first).
extractWords = sentence.split(' ')
reversedList: list[str] = extractWords[::-1]
reversedSentence: str = ' '.join(reversedList)
print(reversedSentence)

#practice problem 2
quote = "Perseverance is the key to success!"

#task 1 Extract the word "Perseverance" from the string.
print(quote[:12])

#task 2 Extract the last 7 characters of the string.
print(quote[-8:])

#task 3 Extract the word "key" using slicing.
print(quote[20:23])

#task 4 Extract the entire string 
# but in reverse order, skipping every 3rd character.
extractString = quote.split(" ")
reverseWords = extractString
reverse_list = ' '.join(reverseWords)
print(reverse_list[::-1][::3])

#task 5 Extract the string starting 
# from the 5th character to the 20th character.
print(quote[5:21])