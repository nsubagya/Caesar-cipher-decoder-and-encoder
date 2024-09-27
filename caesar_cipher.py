#%%writefile caesar_cipher.py #if this is a jupiter note book
import streamlit as st
import string
import nltk
from nltk.corpus import words

nltk.download('words')

def decrypt_caesar_cipher(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            decrypted_char = chr((ord(char) - ord('A' if is_upper else 'a') - shift)%26 + ord('A' if is_upper else 'a'))
            plaintext += decrypted_char
        elif char.isdigit():
            decrypted_char = chr((ord(char) - shift - ord('0')) % 10 + ord('0'))
            plaintext += decrypted_char
        elif char in string.punctuation:  # Handle basic symbols
            symbol_index = string.punctuation.index(char)
            decrypted_char = string.punctuation[(symbol_index - shift) % len(string.punctuation)]
            plaintext += decrypted_char
        #elif char in string.punctuation:
            #decrypted_char = chr((ord(char) - shift) % len(string.punctuation))
            #plaintext += decrypted_char
        else:
            plaintext += char
    
    return plaintext


def encrypt_caesar_cipher(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():#if ord(char) >= 65 and ord(char) <= 122:
            is_upper = char.isupper()
            encrypted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift)%26 + ord('A' if is_upper else 'a'))
            ciphertext += encrypted_char
        elif char.isdigit():
            encrypted_char = chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
            ciphertext += encrypted_char
        elif char in string.punctuation:  # Handle basic symbols
            symbol_index = string.punctuation.index(char)
            encrypted_char = string.punctuation[(symbol_index + shift) % len(string.punctuation)]
            ciphertext += encrypted_char
        #elif char in string.punctuation:
            #encrypted_char = chr((ord(char) + shift) % len(string.punctuation))
            #ciphertext += encrypted_char
        else:
            ciphertext += char
    
    return ciphertext

def Decrypt_caesar_cipher_automation(ciphertext):
    from nltk.corpus import words

    english_words = set(words.words())


    #ciphertext = "W zcjs mci"
    max_english_word_count = 0
    best_shift = 0
    all_dec_text=[]
    for shift in range(26):
        decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
        all_dec_text.append((shift,decrypted_text))
        decrypted_words = decrypted_text.split() 
        english_words_in_decrypted_text = [word for word in decrypted_words if word.lower() in english_words]
        english_words_count = len(english_words_in_decrypted_text)
        if english_words_in_decrypted_text:
            #found_english_word = True
            #english_meaning_text = " ".join(english_words_in_decrypted_text)
            #print("Shift:", shift, "- Decrypted Text:", decrypted_text)
            if english_words_count > max_english_word_count:
                max_english_word_count = english_words_count
                best_shift = int(shift)


        #else:
            #print("Shift:", shift, "- No English words found in any decrypted text.")
    #return best_shift, all_dec_text
    return best_shift, all_dec_text, decrypt_caesar_cipher(ciphertext, best_shift)
    #return print("best shift:",best_shift, "- Best Decrypted Text:", decrypted_text(ciphertext,best_shift))#,all_dec_text
