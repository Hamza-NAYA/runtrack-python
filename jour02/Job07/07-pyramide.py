
import string

alphabet = string.ascii_lowercase*10

n = len(alphabet)

for i in range(n):
    letters = alphabet[:i*1+1]
    print(letters)