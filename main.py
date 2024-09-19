import pandas as pd
from barrier import barrier

options = pd.read_excel('data/elements.xlsx', sheet_name='опции')

chanel = 2 if options['двуканальные барьеры'][0] == 'да' else 1

print(barrier)


