file_path = 'Tubes\PDA.txt'
arr=[]

#Membaca PDA lalu memindahkan ke array sementara
with open(file_path, 'r') as file:
    # Membaca file baris per baris
    for line in file:
        arr.append(line)

#Mengambil state dari array PDA untuk dipindahkan ke array state
arrState=[]
for i in range (len(arr[0])):
    if(i%2==0):
        arrState.append(arr[0][i])

#Mengambil input word dari array PDA untuk dipindahkan ke array input
arrInput=[]
temp=""
for i in range (len(arr[1])):
    if(arr[1][i]==" "):
        arrInput.append(temp)
        temp=""
    else:
        temp=temp+arr[1][i]

#Mengambil stack symbol dari array PDA untuk dipindahkan ke array symbol
arrSymbol=[]
for i in range (len(arr[2])):
    if(i%2==0):
        arrSymbol.append(arr[2][i])

startState = arr[3] # Mengambil start state
startStack = arr[4] # Mengambil start stack
acceptState = arr[5] # Mengambil accept state

#Mengambil list production dari array PDA untuk dipindahkan ke array list production
arrListProduction = []
for i in range (len(arr)):
    temp2=[]
    i = i+6
    print(arr[i])
    for j in range (len(arr[i])):
        if(arr[i][j]==" "):
            temp2.append(temp)
            temp=""
        else:
            temp=temp+arr[i][j]
    print(temp2)
    i = i - 6
print(arrListProduction)


