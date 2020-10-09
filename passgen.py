import random, string, sys, pyperclip

# ensures that the string len is copied before continuing the program
if len(sys.argv) < 2 :
    print (f'Usage passgen.py [int] - number of characters in the string')
    sys.exit()

# the desired stringlen
userinput = int(sys.argv[1])

def randomstring(stringlen):
    '''
    randomstring is a function that takes in the stringlen of a desired randomstring and returns the string

    input: stringlen int
    output: string str

    return: string
    '''
    numbers = '0123456789'
    char = string.ascii_letters + string.punctuation + numbers + string.ascii_letters.upper()
    return ''.join(random.choice(char) for x in range(stringlen))


thestring = randomstring(userinput)

pyperclip.copy(thestring)
print('Random string {thestring} of length{userinput} has been copied and is ready for deploymment')
