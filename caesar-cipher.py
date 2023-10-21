def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            case = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - case + shift) % 26 + case)
        else:
            result += char

    return result

plaintext = input("Enter the text to encrypt/decrypt: ")
shift = int(input("Enter the shift amount (positive for encryption, negative for decryption): "))

encrypted_text = caesar_cipher(plaintext, shift)

print(f"\nOriginal text: {plaintext}")
print(f"Shift amount: {shift}")
print(f"Result: {encrypted_text}")
