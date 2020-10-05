import pandas as pd
import numpy as np

datafrem = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/CHAPTER+4+-+missing+value+-+public+data+covid19+.csv")
daxcel = pd.read_excel("C:/Users/Jungle Kidd/Documents/Coba.xlsx")

print(datafrem.info())
print("#################### DATA_CSV INFO\n")
print(daxcel.info())
print("#################### DATA_EXCEL INFO\n")

missingvalue = datafrem.isna().sum()
print(missingvalue)
print("#################### DATA_CSV MISSING VALUE\n")
missingvalue_xlsx = daxcel.isna().sum()
print(missingvalue_xlsx)
print("#################### DATA_XLSX MISSING VALUE\n")

print(datafrem.shape)
datafrem2 = datafrem.dropna(axis=1, how='all')
print(datafrem2.shape)
datafrem3 = datafrem.dropna(axis=1)
print(datafrem3.shape)
print("#################### DATAFRAME SHAPE\n")

print(datafrem["country_region"].unique())
print("#################### DATAFRAME UNIQUE\n")

ts = pd.Series({
   "2020-01-01":9,
   "2020-01-02":np.nan,
   "2020-01-05":np.nan,
   "2020-01-07":24,
   "2020-01-10":np.nan,
   "2020-01-12":np.nan,
   "2020-01-15":33,
   "2020-01-17":np.nan,
   "2020-01-16":40,
   "2020-01-20":45,
   "2020-01-22":52,
   "2020-01-25":75,
   "2020-01-28":np.nan,
   "2020-01-30":np.nan
})
# Cetak time series
print("Awal:\n", ts)
print("\n")
# Isi missing value menggunakan interpolasi linier
ts = ts.interpolate()
# Cetak time series setelah interpolasi linier
print("Setelah diisi missing valuenya:\n", ts)
print("#################### SERIES INTERPOLATION\n")
