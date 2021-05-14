import sys
from pyiso4.ltwa import Abbreviate

if len(sys.argv) != 2:
    raise Exception('one argument expected')

abbrv = Abbreviate.from_files('LTWA_20170914.csv', 'stopwords.txt')

# print(abbrv.ltwa_prefix.search('vitro'))

print(abbrv(sys.argv[1]))