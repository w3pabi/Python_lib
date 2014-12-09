#Maketrans() and translate()
#Maketrans string.maketrans('orignal_string', 'change_string')
#Translate change characters orignal_string to change_string

import string

leet = string.maketrans('abegiloprstz', '463611092572')
s = 'The quick brown fox jumped over the lazy dog.'

print s
print s.translate(leet)
