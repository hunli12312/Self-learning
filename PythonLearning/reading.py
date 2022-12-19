employee_file = open("read.txt", "r")
print(employee_file.read()) #.read() .realine() .readlines() .readable()
# for readline() it works one after one overlapping
for employee in employee_file.readline():
    print (employee)
employee_file.close()