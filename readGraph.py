#read csv
#graph 1 column

import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'


with open(filename) as f:
    
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    highs = []

    for row in reader:
        highs.append(row[1]) #row 2 but it means grab the column 2
    print(highs)
    
#set figure size
    
fig = plt.figure(dpi = 128,figsize = (10,6))

plt.plot(highs, c= 'red')

plt.title("daily high temp", frontsize = 24)

plt.xlabel(' ',frontsize = 16)

plt.ylabel('temp F',frontsize = 16)

plt.tick_params(axis='nptj',which = 'major', labelsize = 16)

plt.show()

