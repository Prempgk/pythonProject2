import itertools
import string
import time


def password_wordlist(start_range=8, end_range=10, file_name="brute.txt"):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '@' + '#' + '$' + '.'
    attempts = 0
    f = open(file_name, 'a')

    for password_length in range(start_range, end_range):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            f.write(guess)
            f.write("\n")
            print(guess, attempts)

    f.close()


start_range = 8
end_range = 10
file_name = "brute_password_list.txt"

start_time = time.time()
password_wordlist(start_range, end_range, file_name)
end_time = time.time()

print(end_time - start_time)