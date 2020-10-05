global_air = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv")
print(global_air.head())
print("#################### PRINT GLOBAL AIR\n")
print(global_air.info())
print("#################### PRINT GLOBAL AIR [INFO]\n")
print(global_air.count())
print("#################### PRINT GLOBAL AIR [COUNT] \n")
global_air_gby = global_air.groupby('source_name').count()
print(global_air_gby.head())
print("#################### PRINT GLOBAL AIR [GROUP BY] \n")

pollution = global_air[['country', 'city', 'pollutant', 'value']].pivot_table(index=['country','city'], columns='pollutant').fillna(0)
print(pollution.head())
print("######################################## PRINT POLLUTION \n")
pollution_mean = pollution.groupby('country').mean()
print(pollution_mean.head())
print("######################################## PRINT POLLUTION MEAN\n")
pollution_std = pollution.groupby('country').std().fillna(0)
print(pollution_std.head())
print("######################################## PRINT POLLUTION STD\n")
pollution_sum = pollution.groupby('country').sum()
print(pollution_sum.head())
print("######################################## PRINT POLLUTION SUM\n")
pollution_nunique = pollution.groupby('country').nunique()
print(pollution_nunique.head())
print("######################################## PRINT POLLUTION NUNIQUE\n")