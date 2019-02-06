def mencariMean(dataset): #jumlahisidata + banyak data
    jumlah=0
    for i in dataset:
        jumlah+=i
    mean=jumlah/(len(dataset))
    return mean

def mencariModus(dataset): #mencari frekuensi angka terbanyak
    countList=[]
    for num in dataset :
        check = False
        for list1 in countList :
            if(list1[0] == num) :
                list1[1] += 1
                check = True
        if(check == False) :
            countList.append([num, 0])
    maxFrequency = 0
    modus = []
    for list1 in countList :
        if (list1[1] > maxFrequency) :
            modus = [list1[0]]
            maxFrequency = list1[1]
        elif (list1[1] == maxFrequency) :
            modus.append(list1[0])
    if (len(modus) == len(countList)) :
        modus = []
    return modus
    
def mencariMedian(dataset): #mencari nilai tengah dari set data
    median = 0
    dataset.sort()
    if(len(dataset)%2 == 1):
        median=dataset[int(len(dataset)/2)]
    else:
        midbawah = dataset[(int(len(dataset)/2))-1]
        midatas = dataset[(int(len(dataset)/2))]
        median = (midbawah+midatas)/2
    return median