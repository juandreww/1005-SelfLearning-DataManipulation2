daframe = pd.DataFrame({
    'Sekolah' : 4*['Tarakanita'] + 4*['Kanisius'],
    'Tim' : ['TarA'] + 2*['TarB'] + ['TarC'] + 2*['KanA'] + ['KanB'] + ['KanC'],
    'Lomba' : 4*['Matematika', 'IPS'],
    'Skor' : 2*[100] + [60,80,70,50,80,90]
}, columns= ['Sekolah','Tim', 'Lomba', 'Skor'])
print(daframe)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ DAFRAME\n")

daframe = daframe.set_index(['Sekolah', 'Tim', 'Lomba'])
print(daframe)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ DAFRAME SET INDEX\n")

daframe_us1 = daframe.unstack()
print(daframe_us1)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ DAFRAME UNSTACK 1\n")
daframe_us2 = daframe.unstack(level='Sekolah').fillna(0)
print(daframe_us2)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ DAFRAME UNSTACK 2\n")
daframe_us3 = daframe.unstack(level=1).fillna(0)
print(daframe_us3)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ DAFRAME UNSTACK 3\n")

daframe_s1 = daframe_us3.stack()
print(daframe_s1)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ DAFRAME STACK\n")
daframe_swap = daframe_s1.swaplevel(1,2)
print(daframe_swap)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ DAFRAME SWAP\n")
daframe_sort =daframe_swap.sort_index()
print(daframe_sort)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@ DAFRAME SORT\n")