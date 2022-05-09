import string, re
#open text file, read mode | read file and split by new line
data = open('input5.txt', 'r').read().split('\n')

'''
match = re.search(pat, str)
r designates raw string
[] match one or more of the characters in this group
.* any character repeated
{3,} repeat at least 3 times
(.) any character
\1 repeat first group in ()
ab|cd match ab or cd
'''

def nice_list():
    nice = 0
    for line in data:
        aeiou = re.search(r'([aeiou].*){3,}', line)
        pair = re.search(r'(.)\1', line)
        bad = re.search(r'(ab|cd|pq|xy)', line)
        if aeiou and pair and not bad:
            nice += 1
    return nice

'''
It contains a pair of any two letters that appears at least twice in the string without overlapping
It contains at least one letter which repeats with exactly one letter between them
(..) any two characters
'''
def second_list():
    nice = 0
    for line in data:
        pair_pair = re.search(r'(..).*\1', line)
        repeat_any_repeat = re.search(r'(.).\1', line)
        if  pair_pair and repeat_any_repeat:
            nice +=1
    return nice

def main():
    print(nice_list())
    print(second_list())

main()