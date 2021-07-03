import sys
from pyiso4.ltwa import Abbreviate, Pattern
from pyiso4.normalize_string import normalize, Level

if len(sys.argv) != 2:
    raise Exception('one argument expected')

abbrv = Abbreviate.from_files('LTWA_20170914-modified.csv', 'stopwords.txt')
# p = Pattern.from_line('médic-	méd.	cat')
# print(p)
# print(abbrv._potential_matches('Médica'))

print(abbrv(sys.argv[1]))