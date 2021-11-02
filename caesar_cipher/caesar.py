import nltk
import re

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

def encrypt(text,k):
    # text = text.lower()
    if k > 25 :
        if k % 25 == 0 :
            k = 25
        else :
            k = k - (25 *(k // 25))
    origin_k = k
    
    new_array=[]
    arr_text = text.split(' ')
    for words in arr_text:
        text_after_encrypt = ''
        for litters in words:
            if ord(litters) + k > 122 :
                k = k - 26
            text_after_encrypt += chr(ord(litters)+k)
            k = origin_k
        new_array.append(text_after_encrypt)
        new_array.append(' ')
    last_string = ''
    last_string = last_string.join(new_array)
    return str(last_string)

def decrypt(text,k):
    # text = text.lower()
    if k > 25 :
        if k % 25 == 0 :
            k = 25
        else :
            k = k - (25 *(k // 25))
    origin_k = k
    
    new_array=[]
    arr_text = text.split(' ')
    for words in arr_text:
        text_after_encrypt = ''
        for litters in words:
            if ord(litters) - k < 97 :
                k =  k - 26 
            text_after_encrypt += chr(ord(litters)-k)
            k = origin_k
        new_array.append(text_after_encrypt)
        new_array.append(' ')
    last_string = ''
    last_string = last_string.join(new_array)
    return last_string

def count_words(text):
    candidate_words = text.split()
    count = 0
    for i in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', i)
        if word.lower() in word_list or word in name_list:
            count += 1

    return count

def crack(encrypted):
    for i in range (0,26):
        text = decrypt(encrypted,i)
        percentage = int(count_words(text) / len(encrypted.split()) * 100)
        if percentage > 50:
            return text 
