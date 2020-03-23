import pandas as pd
import numpy as np
import re

# Comprueba si la columna dada y las incluidas en la función, son iguales, es decir, contienen los mismos datos.
def check_dupl_caseNumber(df,col):
    results = []
    index = 0
    for value in col:
        if value == df['Case Number.1'][index] and value == df['Case Number.2'][index]:
            index += 1
            results.append('True')
        else:
            index += 1
            results.append('False')
    index_falsy = []
    for ind,result in enumerate(results):
        if result == 'False':
            index_falsy.append(ind)
    print(f'There are {len(index_falsy)} differences from {len(results)} total rows.')
    for ind in index_falsy:
        print('\nFALSE:')
        print(df['Case Number'][ind])
        print(df['Case Number.1'][ind])
        print(df['Case Number.2'][ind])

# Comprueba si la columna dada y las incluidas en la función, son iguales, es decir, contienen los mismos datos.
def check_dupl_href(df,col):
    results = []
    index = 0
    for value in col:
        if value == df['href formula'][index]:
            index += 1
            results.append('True')
        else:
            index += 1
            results.append('False')
    index_falsy = []
    for ind,result in enumerate(results):
        if result == 'False':
            index_falsy.append(ind)
    print(f'There are {len(index_falsy)} differences from {len(results)} total rows.')
    for ind in index_falsy:
        print('\nFALSE:')
        print(df['href'][ind])
        print(df['href formula'][ind])

# Elimina los espacios que haya delante:
def first_space(serie):
    return serie.replace("^\s", "")