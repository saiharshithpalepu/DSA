#average temperature calculation

numDays = int(input('Please specify for how many days the temperatures to be taken:'))

temp=[]
total=0

for i in range(0,numDays):
    temp1=int(input(f"day's {i+1} temperature:"))
    temp.append(temp1)
    total+=temp1

average_temp=round((sum(temp)/len(temp)),2)
print(f"average: {average_temp}")

count=[i for i in temp if i>average_temp]

print(f"the no of days which have greater tempature than the average temperature: {len(count)}")