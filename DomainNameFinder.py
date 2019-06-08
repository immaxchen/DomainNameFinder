import time
import itertools
import subprocess

letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
digits = '0123456789'
alphanumerics = letters + digits
two_letter_words = [line.rstrip('\n') for line in open('two_letter_words.txt')]
three_letter_words = [line.rstrip('\n') for line in open('three_letter_words.txt')]
four_letter_words = [line.rstrip('\n') for line in open('four_letter_words.txt')]

def wordsmaker(*slots):
    for strs in itertools.product(*slots):
        yield ''.join(strs)

def registered(domainname):
    proc = subprocess.Popen(['whois', domainname], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    text = proc.stdout.read().decode()
    return 'No match for \"' not in text

def checknames(*slots, tld='.com'):
    print('Available Names for {0} :'.format(tld))
    tstart = time.time()
    for word in wordsmaker(*slots):
        name = word + tld
        if not registered(name):
            print(word, end='  ')
    print('\nElapsed Time :', time.time() - tstart)

