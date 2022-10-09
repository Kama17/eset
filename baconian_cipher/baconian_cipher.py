import sys
import random
import os
from tokenize import String

cipher = {'uuuuu': 'a', 'uuuul': 'b', 'uuulu': 'c', 'uuull': 'd', 'uuluu': 'e', 'uulul': 'f', 'uullu': 'g', 
        'uulll': 'h', 'uluuu': 'i', 'uluul': 'j', 'ululu': 'k', 'ulull': 'l', 'ulluu': 'm', 'ullul': 'n', 
        'ulllu': 'o', 'ullll': 'p', 'luuuu': 'q', 'luuul': 'r', 'luulu': 's', 'luull': 't', 'luluu': 
        'u', 'lulul': 'v', 'lullu': 'w', 'lulll': 'x', 'lluuu': 'y', 'lluul': 'z', 'llllu': '.', 'lllll': ' '}


def read_file() -> str:
    """Returns the text or error if the file can't be opened.

    Preconditions:
    - file with .txt extension.
    - file passed in as a system argument.
    Postconditions: The output is the text of file as string.
    """
    try:
        file = input(f"Please enter relative or absolute file path file=")
        path = os.path.join(file)
        with open(path,"r") as file:
            contents = file.read()
    except FileNotFoundError:
        sys.exit("File cannot be open")
    return contents


def get_txt_to_decode(user_text:str) -> str:
    """"Returns the text where alphabet letters are decoded from the corresponding cipher sequence.
    
    Preconditions: user_text = any alphabet letter.
    Postconditions: The output converts the alphabet letters to decoded text.
    """
    plain_text = ""
    for letter in user_text:
        letter_as_num = ord(letter)
        if 65 <= letter_as_num <= 90:
            plain_text += "u"
        elif 97 <= letter_as_num <= 122:
            plain_text += "l"
    return plain_text


def decode(text_to_decode:str) -> str:
    """"Returns the decoded text based on the cipher dictionary.
    
    Preconditions:
    - text_to_decode must be the sequence of the cipher letters.
    - text_to_decode is read in a sequence of 5 letters.
    Postconditions: The output is the decoded text based on the cipher sequence.
    """
    decoded_message = ""
    i = 0
    while(i < len(text_to_decode)):
        substring_of_5 = text_to_decode[i: i + 5]
        
        if substring_of_5 in cipher.keys():
            if cipher[substring_of_5] == " ":
                decoded_message += " "
            decoded_message += cipher[substring_of_5]
        i += 5
    print(f"Your decoded massage is: {decoded_message}")


def encode(user_text:str) -> str:
    """Returns the encoded text based on the cipher disctionary.
    
    Preconditins: user_text = text to be encoded.
    Postconditions: The output is the  encoded text based on the cipher dictionary with randomly chosen ASCII characteres.
    """
    encoded_massage = ""
    for i in user_text:
        encoded_massage += random_char()
        for key, value in cipher.items():
            if value == i.lower():
                for char in key:
                    encoded_massage += random_letter(char)
    print(f"Your encoded message is: {encoded_massage}")


def random_letter(letter: String[1]) -> String[1]:
    """Returns the random letter base on the ASCII integer value
    
    Preconditions: 
     - letter = "u" or "l"
     - "u" is between uppercase alphabetic letters
     - "l" is between lowercase alphabetic letters
    Postconditions: The output is a randomly chosen letter.
    """
    if letter == "u":
        plain_text = random.randint(65,90)
    elif letter == "l":
        plain_text = random.randint(97,122)
    return chr(plain_text)


def random_char() -> String[1]:
    """Returns randomly chosen character corresponding to the 32,33,46,63 ASCII values.
    
    Preconditions: ASCII character of the choice.
    Postconditions: The output is a randomly chosen value form rand_ascii list.  
    """
    rand_ascii = [32,33,46,63]
    char = random.choice(rand_ascii)
    return chr(char)


if __name__ == '__main__':
    while True:
        choice = input("Hello and welcome to the Bacoinian Cipher Encoder and Decoder program!\nWould you like to Decode(1) or Encode(2) message? (1/2?) ")
        input_choice = input(f"Great!!! Do you want to type in your massage(1) or upload(2) text file? (1/2?) ")
        if choice == "1":
            if input_choice == "1":
                user_text = input("Enter text to be decoded: ")
                cipher_txt = get_txt_to_decode(user_text)
                message = decode(cipher_txt)
            elif input_choice == "2":
                file_txt = read_file()
                cipher_txt = get_txt_to_decode(file_txt)
                message = decode(cipher_txt)
        elif choice == "2":
            if input_choice == "1":
                user_text = input("Enter text to be encode: ")
                encode(user_text)
            elif input_choice == "2":
                file_txt = read_file()
                encode(file_txt)
        else:
            print("Please select correct option!")

        play = input("Would you like to try again? (Y/N?)").lower()
        if play == "n":
            break
