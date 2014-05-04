import itertools
from string import ascii_lowercase

def bruteforce(alphabet, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(alphabet, repeat=i)
        for i in range(1, maxlength + 1)))

if __name__ == "__main__":
    alphabet = ascii_lowercase
    count = 0
    for attempt in bruteforce(alphabet, 5):
        count += 1
    print count