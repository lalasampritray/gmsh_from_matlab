import csv
import matplotlib.pyplot as plt
f = open("msh.txt", "w")
with open('msh.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    x=[]
    y=[]
    for row in csv_reader:
        line_count += 1 
        f.write('Point({})={{{},0,{},1}} \n'.format(line_count,row[0],row[1]))
        x.append(row[0])
        y.append(row[1])
    
    print(f'Processed {line_count} lines.')

z = plt.scatter(x,y)
plt.show(z)