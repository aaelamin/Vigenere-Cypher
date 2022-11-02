
from string import punctuation, digits, ascii_uppercase


def cypher(plain_text, key):
    """
    The function takes the "plain_text" and "key" as parameters and uses the
    Vigenere Cypher principals to encrypt and return the given text.
    parameter: plain_text - string, key - string
    return: encrypted_message - string
    """
    encrypted_message = ""
    # Create two dictionaries that convert characters from letters to integers
    # and vice-versa
    index_character = dict(zip(range(0, 26), ascii_uppercase))
    character_index = dict(zip(ascii_uppercase, range(0, 26)))

    # Convert the plain_text and key to number using the second dictionary.
    text_index = ([character_index.get(letter) for letter in plain_text if
                   letter in character_index.keys()])
    key_index = ([character_index.get(letter) for letter in key if
                  letter in character_index.keys()])

    # The following code adds the numbers in text_index and key_index to shift
    # the letter
    for i in range(len(text_index)):
        value = (text_index[i] + key_index[i % len(key)]) % 26
        encrypted_message += index_character[value]
    return encrypted_message


def main():
    # Ask user for input and remove white spaces and convert to upper
    text = (input("Enter the text you want to encrypt:\n").upper().
            replace(" ", ""))
    for i in text:
        if i in punctuation or i in digits:
            text = text.replace(i, "")  # Remove numbers and punctuations
    key = input("Enter the key for encryption:\n").upper().replace(" ", "")
    # Call the cypher function and assign it to the variable "encryption".
    encryption = cypher(text, key)
    print("Your encrypted message is: \n" + encryption)


main()
