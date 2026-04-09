print('Greeting function')

def greet(name):
    print("Hello" + name + ".Good Morning")
greet('Fatema')
greet('Tabina')

print('Finding absolute value')

def absolute_num(num):
    if num>=0:
        return num
    else:
        return -num
print("Absolute value of the number is" ,absolute_num(89))
print("Absolute value of the number is" ,absolute_num(-189))

print('Finding palindrome words')
def palindrome(word):
    if word==word[::-1]:
      return True
    else:
        return False


if palindrome('madam'):
 print('The word is Pelindrome')
else:
 print('The word is not Pelindrome')
