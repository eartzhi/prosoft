import pandas as pd

barrier_np = pd.read_excel('data/elements.xlsx', sheet_name='барьеры New Power')
barrier_ch = pd.read_excel('data/elements.xlsx', sheet_name='барьеры Chenzhu')
options = pd.read_excel('data/elements.xlsx', sheet_name='опции')


barrier = barrier_ch if options['тип барьеров'][0] == 'Chenzhu' else barrier_np
barrier = barrier[barrier['каналов'] == 2] if options['двуканальные барьеры'][0] == 'да' \
    else barrier[barrier['каналов'] == 1]