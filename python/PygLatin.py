pyg = 'ay'
original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first in ['a','e','i','o','u'] :
        print word + pyg
    else :
        print word[1:] + first + pyg
else:
    print 'empty'