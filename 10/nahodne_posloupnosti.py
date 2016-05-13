import csv

for i in range(1,8):
    filename = ('random'+str(i)+".txt")
    data = None
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            data = row

    # print(data)
    cetnost = [0 for i in range(6)]
    for x in row:
        cetnost[int(x)-1]+=1
    # print(len(data),cetnost)

    sum = 0
    sum2 = 0
    for O_i in cetnost:
        E = len(data)/6
        sum  +=((O_i - E)**2)/E
        sum2 +=((O_i - E)**2)/O_i

    chi_squared = sum
    print(filename,"chi squared",chi_squared,sum2)
