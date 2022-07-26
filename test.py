import pandas as pd
from icecream import ic
from itertools import chain
from collections import defaultdict


csv_test = pd.read_csv('./save/reviews/IT모바일.csv')

dict3 = defaultdict(list)

for k, v in chain(csv_test):
    dict3[k].append(v)

for k, v in dict3.items():
    print(k, v)


