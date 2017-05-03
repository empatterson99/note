title = "Days of the Week\n"
path = "days.txt"
days_file = open(path,'r')
days = days_file.read()
new_path = "new_days.txt"
new_days = open(new_path,'a+')
new_days.write('5')
print(title)


print(days)
days_file.close()
new_days.close()
