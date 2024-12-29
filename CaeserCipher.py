def caesar_cipher_encrypt(text, shift):
    """
    Encrypts a given text using Caesar Cipher.

    Args:
        text (str): The text to encrypt.
        shift (int): The number of positions to shift each character.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the ASCII offset (65 for uppercase, 97 for lowercase)
            ascii_offset = 65 if char.isupper() else 97

            # Shift the character and wrap around using modulo
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            # Non-alphabetic characters are added as-is
            encrypted_text += char

    return encrypted_text

# Example usage
if __name__ == "__main__":
    text_to_encrypt = input("Enter the text to encrypt: ")
    shift_value = int(input("Enter the shift value: "))

    encrypted = caesar_cipher_encrypt(text_to_encrypt, shift_value)
    print(f"Encrypted text: {encrypted}")
