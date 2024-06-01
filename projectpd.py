#importing pandas
import pandas as pd
countries = set()
short_city_names=set()



#converting the csv file into dataframe
df=pd.read_csv('/Users/nickwill/Downloads/simplemaps_worldcities_basicv1.77/worldcities.csv')


user=input("print csv file?")
if user=="Yes":
   print(df)

#getting the index value of cities labeles as primary in the 'capital' column
primary_cities_index=df[df['capital']=='primary'].index


for index in primary_cities_index:
   country_name = df.loc[index, 'country']
   capital_city = df.loc[index, 'city']
   if len(capital_city) < 6:
      short_city_names.add(country_name)

print("countries with short capital city names:")
print(short_city_names)


#grouping all countries and their corresponding values in a pandas array
groupe_countries = df.groupby('country')


for group in groupe_countries:
    if (group[1]['lat'].astype(float) + group[1]['lng'].astype(float)).sum() > 100:
        country = group[0]
        countries.add(country)
print(countries)



