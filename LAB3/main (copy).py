def substitute(text, key_map):
  return ''.join([key_map.get(c, c) for c in text])

def permute(text): 
  return text[::-1]

def encrypt(message, key_map, rounds=3):
  """
  Encrypt the message with multiple rounds of substitution and permutation.
  """
  for _ in range(rounds):
      message = substitute(message, key_map)
      message = permute(message)
  return message

def decrypt(ciphertext, key_map, rounds=3):
  """
  Decrypt the message by reversing the rounds of permutation and substitution.
  """
  for _ in range(rounds):
      ciphertext = permute(ciphertext)
      ciphertext = substitute(ciphertext, {v: k for k, v in key_map.items()})
  return ciphertext


key_map = {
  'G': 'Q',
  'o': 'x',
  'B': 'K',
  'u': 'z',
  'l': 'v',
  'd': 'p',
  'g': 'w',
  's': 'n',
  '!': '$'
}

def main():
  print("Welcome to the MIXnMatch Cipher!")

  
  message = input("Enter the message to encrypt: ")
  rounds = int(input("Enter the number of rounds: "))

 
  encrypted = encrypt(message, key_map, rounds)
  print(f"\nEncrypted message: {encrypted}")

  
  decrypted = decrypt(encrypted, key_map, rounds)
  print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
  main()
