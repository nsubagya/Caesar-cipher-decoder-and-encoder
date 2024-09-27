# app.py

import streamlit as st
from caesar_cipher import encrypt_caesar_cipher, decrypt_caesar_cipher, Decrypt_caesar_cipher_automation

# Streamlit interface
st.title("Caesar Cipher Encryption and Decryption")

# Create input fields and user interface
option = st.selectbox("Choose an option:", ["Encrypt", "Decrypt", "Automated Decryption"])
input_text = st.text_area("Enter your text here:")

if option != "Automated Decryption":
    shift_value = st.slider("Select the shift value:", 1, 25, 3)

if st.button("Submit"):
    if option == "Encrypt":
        encrypted_text = encrypt_caesar_cipher(input_text, shift_value)
        st.subheader("Encrypted Text")
        st.write(encrypted_text)
    elif option == "Decrypt":
        decrypted_text = decrypt_caesar_cipher(input_text, shift_value)
        st.subheader("Decrypted Text")
        st.write(decrypted_text)
    elif option == "Automated Decryption":
        best_shift, all_decrypted_texts, best_decrypted_text = Decrypt_caesar_cipher_automation(input_text)
        #best_shift, all_decrypted_texts = Decrypt_caesar_cipher_automation(input_text)
        st.subheader("Best Shift Value")
        st.write(best_shift)
        st.subheader("Best Decrypted Text")
        st.write(best_decrypted_text)
        st.subheader("All Possible Decryptions")
        for shift, text in all_decrypted_texts:
            st.write(f"Shift: {shift} - Decrypted Text: {text}")
