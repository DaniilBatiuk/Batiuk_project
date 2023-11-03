def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()            
            char_num = ord(char.lower()) - ord('a')
            shifted_char = chr(((char_num + shift) % 26) + ord('a'))

            if is_upper:
                shifted_char = shifted_char.upper()

            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

text = input("Введіть рядок для шифрування: ")
    
while True:
    try:
        shift = int(input("Введіть значення зсуву (1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Некоректне значення зсуву. Введіть число в діапазоні від 1 до 25.")
    except ValueError:
        print("Некоректне значення зсуву. Введіть число в діапазоні від 1 до 25.")
        
encrypted_text = caesar_cipher(text, shift)
print("Зашифрований текст:", encrypted_text)


#questions

s1= 'Where are the snows of yesteryear?' 
s2 = s1.split() 
s3 = sorted(s2) 
print(s3[1])


s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)