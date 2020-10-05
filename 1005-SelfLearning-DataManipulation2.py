import pandas as pd

daframe = pd.DataFrame({
    'Sekolah' : 4*['Tarakanita'] + 4*['Kanisius'],
    'Tim' : ['TarA'] + 2*['TarB'] + ['TarC'] + 2*['KanA'] + ['KanB'] + ['KanC'],
    'Lomba' : 4*['Matematika', 'IPS'],
    'Skor' : 2*[100] + [60,80,70,50,80,90]
}, columns= ['Sekolah','Tim', 'Lomba', 'Skor'])
print(daframe)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ DAFRAME\n")

#for column in daframe.columns:
#   print(daframe[column].unique())
#print("@@@@@@@@@@@@@@@@@@@@@@@@@@ UNIQUE COLUMNS\n")

pivoting = daframe.pivot(index='Lomba', columns='Skor', values='Tim').fillna(0)
print(pivoting)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ PIVOTING\n")

multi_pivot = daframe.pivot(index='Tim', columns='Lomba')
print(multi_pivot)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ MUTLI PIVOTING\n")

pivot_mean = daframe.pivot_table(index='Sekolah', columns='Lomba', values='Skor', aggfunc='mean')
pivot_median = daframe.pivot_table(index='Sekolah', columns='Lomba', values='Skor', aggfunc='median')
print(pivot_mean)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ PIVOT MEAN\n")
print(pivot_median)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ PIVOT MEDIAN\n")

pivot_reindex = pivot_mean.reset_index()
print(pivot_reindex)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ PIVOT RESET INDEX 1\n")
pivot_melt2 = pd.melt(pivot_reindex)
print(pivot_melt2)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ PIVOT MELT 1\n")
pivot_melt3 = pd.melt(pivot_reindex, id_vars='Sekolah')
print(pivot_melt3)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ PIVOT MELT 2 [ID VARS]\n")
pivot_melt4 = pd.melt(pivot_reindex, id_vars='IPS')
print(pivot_melt4)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ PIVOT MELT 3 [ID VARS] & [VALUE VARS]\n")
pivot_melt5 = pd.melt(pivot_reindex, value_vars=['IPS'])
print(pivot_melt5)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ PIVOT MELT 4 [VALUE VARS]\n")
pivot_melt6 = pd.melt(pivot_reindex, id_vars='Sekolah', value_vars=['IPS', 'Matematika'], var_name='Lombe', value_name='Skor')
print(pivot_melt6)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ PIVOT MELT 5 \n")