import csv

countries = set()
short_city_names = set()


with open('/Users/nickwill/Downloads/simplemaps_worldcities_basicv1.77/worldcities.csv', 'r', newline='') as csvfile:
    world_cities = csv.reader(csvfile)

    # skip the header row
    next(world_cities)
  
    
    # process rows to check conditions
    for row in world_cities:
        city = row[0]
        country = row[4]
        lat_str = row[2]
        lng_str = row[3]
        capital = row[8]
        print(row)

         

            # if capital city contains less than 6 letters add country to short_city_names set
            if capital == "primary" and len(city) < 6:
                short_city_names.add(country)


            
            # check if latitude and longitude are not empty strings
            if lat_str and lng_str:
            lat = float(lat_str)  
            lng = float(lng_str)             # if lat + lng > 100 add given country name to countries set
            
            if lat + lng > 100:
               countries.add(country)



print("Countries with short capital city names:")
print(short_city_names)

print("Countries containing cities with lat+lng values > 100:")
print(countries)


