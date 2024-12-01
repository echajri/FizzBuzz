star_year = int(input("entrer nomber star year: "))
end_year = int(input("entrer nomber end year: "))
for year in range (star_year,end_year +1):
    if year % 4 == 0 :
        print(f"{year}, this is a leap  year ")
    elif year % 100 == 0 :
        print(f"{year}, this is a leap  year ")
    elif year  % 400 == 0 :
         print(f"{year}, this is a leap  year ")
    else:
        print(f"{year}, this  is not a leap year ")