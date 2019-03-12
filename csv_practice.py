'''learning to work with a CSV file'''
'''to open csv files, you use the module CSV
that can be invoked thusly
import csv
as it's built into Python
from there, you can write the rest of your program
here is an example of how to open a csv file, and pass the variable to the module:'''


'''--------------------------------------'''
'''DATA FILES AND SUMMARY STATISTICS'''
import csv
#precision 2    #sets precision to two floating point decimal printing places
#NOTE: the above only works in iPython/Jupyter Notebooks...it won't work in Atom

with open("mpg.csv") as csvfile:    #read in the practice file
    mpg = list(csv.DictReader(csvfile)) #convert to list of dictionaries

#view first three elements of the list:
print(mpg[:3])

'''you can find TOTAL NUMBER OF ENTRIES simply by using length'''
len(mpg)

'''you can VIEW THE COLUMN NAMES by using the KEYS METHOD'''
mpg[0].keys()

'''if you want to find average city MPG, across all cars in the CSV file'''
sum(float(d["cty"]) for d in mpg / len(mpg)
#the above is SUM THE CITY MPG ENTRY across all the dictionaries in the list, and divide by length
#because values in a dictionary are strings, you need to convert to FLOAT to perform mathematical operations

#if you want to find average highway MGP, it looks much the same
sum(float(d["hwy"]) for d in mpg / len(mpg)

#say you want to know what the average city MPG is, GROUPED by the number of cylinders that a car has
cylinders = set(d["cyl"]) for d in mpg)
print(cylinders)
#this will display 4, 5, 6, and 8 cylinders
#next create an empty list to store calculations:
city_mpg_by_cyl = []
for i in cylinders:
    sum_mpg = 0
    cyl_type_count = 0
    for d in mpg:
        if d["cyl"] == c:
            sum_mpg += float(d["cty"])
            cyl_type_count += 1
    city_mpg_by_cyl.append((c, sum_mpg / cyl_type_count))

city_mpg_by_cyl.sort(key=lambda x: x[0])
print(city_mpg_by_cyl)
