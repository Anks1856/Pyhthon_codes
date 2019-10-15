# my_word = "madam"
my_word = str(input("enter your word "))
if my_word == my_word[::-1]:
    print("your word is palindrome")
else:
    print("your word is not palindrome")
