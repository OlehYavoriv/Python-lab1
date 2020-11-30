string = input("Enter the message: ")
small_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big_alphabet = ['A','B','C','D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small_ua_alphabet = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з','и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р','с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
big_ua_alphabet = ['А','Б','В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я']
number =['0','1','2','3','4','5','6','7','8','9']

key=3
cipher=""
plain=""

for i in string:
    if i in big_alphabet:
        cipher += big_alphabet[(big_alphabet.index(i) + key) % len(big_alphabet)]
    elif i in small_alphabet:
        cipher += small_alphabet[(small_alphabet.index(i) + key) % len(small_alphabet)]
    elif i in small_ua_alphabet:
        cipher += small_ua_alphabet[(small_ua_alphabet.index(i) + key) % len(small_ua_alphabet)]
    elif i in big_ua_alphabet:
        cipher += big_ua_alphabet[(big_ua_alphabet.index(i) + key) % len(big_ua_alphabet)]
    elif i in number:
        cipher += number[(number.index(i) + key) % len(number)]
    else:
        cipher += i
for i in cipher:
    if i in big_alphabet:
        plain += big_alphabet[(big_alphabet.index(i) - key) % len(big_alphabet)]
    elif i in small_alphabet:
        plain += small_alphabet[(small_alphabet.index(i) - key) % len(small_alphabet)]
    elif i in small_ua_alphabet:
        cipher += small_ua_alphabet[(small_ua_alphabet.index(i) - key) % len(small_ua_alphabet)]
    elif i in big_ua_alphabet:
        cipher += big_ua_alphabet[(big_ua_alphabet.index(i) - key) % len(big_ua_alphabet)]
    else:
        plain += i
print("Your message is :", cipher)
