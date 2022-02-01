import itertools
import string
import hashlib
from time import time

class word():
    def re():
        str = input("Enter an MD5 code to be decoded: ")
        #result = hashlib.md5(str.encode())

        #print("The hexadecimal equivalent of hash is : ", end ="")
        #end = result.hexdigest()
        return str

class guess_word():
    def gu(x):
        result = hashlib.md5(x.encode())

        #print("The hexadecimal equivalent of hash is : ", end ="")
        #gue = result.hexdigest()
        return result.hexdigest()

class comp():
    def guess_password(real):
        global start
        start = time()
        chars = string.ascii_letters + string.digits
        attempts = 0
        for password_length in range(1, 9):
            for guess in itertools.product(chars, repeat=password_length):
                attempts += 1
                guess = ''.join(guess)
                result = hashlib.md5(guess.encode())
                if result.hexdigest() == real:
                    return 'password is {}. found in {} guesses.'.format(guess, attempts)
                print(guess, result.hexdigest(), attempts)

print(comp.guess_password(word.re()))
end = time()
time = end - start
print("Time: %s seconds" % time)
