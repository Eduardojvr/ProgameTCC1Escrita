listaDc = {
    "DC1": [],
    "DC2": [],
    "DC3": [],
    "DC4": [],
    "DC5": [],
    "DC6": [],
    "DC7": [],
    "DC8": []
}
count=0
tmp = 0
resultado = []

for i in range(8):
    for j in range(3):
        count+=1
        for a in range(11):
            val = input("DC"+str(i+1)+" --> Questão "+ str(count)+ "-> Quantas pessoas votaram "+str(a)+ "? ")
            listaDc["DC"+str(i+1)].append(val)

c=1
for m in range(8):
    for l in range(0,11):
        tmp = tmp+ (int(listaDc["DC"+str(m+1)][l]) * (c))
        c+=1
    resultado.append(tmp)
    tmp=0
    c=1
    for f in range(11, 22):
        tmp = tmp+ (int(listaDc["DC"+str(m+1)][f]) * (c))
        c+=1
    resultado.append(tmp)
    c=1
    tmp=0
    for g in range(22, 33):
        tmp = tmp+ (int(listaDc["DC"+str(m+1)][g]) * (c))
        c+=1
    resultado.append(tmp)
    c=1
    tmp=0

print(resultado)

dc1 = (int(resultado[0])+ int(resultado[1])+int(resultado[2])) / 3
dc2 = (int(resultado[3])+ int(resultado[4])+int(resultado[5])) / 3
dc3 = (int(resultado[6])+ int(resultado[7])+int(resultado[8])) / 3
dc4 = (int(resultado[9])+ int(resultado[10])+int(resultado[11])) / 3
dc5 = (int(resultado[12])+ int(resultado[13])+int(resultado[14])) / 3
dc6 = (int(resultado[15])+ int(resultado[16])+int(resultado[17])) / 3
dc7 = (int(resultado[18])+ int(resultado[19])+int(resultado[20])) / 3
dc8 = (int(resultado[21])+ int(resultado[22])+int(resultado[23])) / 3

print(dc1)
print(dc1)
print(dc1)
print(dc1)
print(dc1)
print(dc1)
print(dc1)
print(dc1)

442
582
529
578

# print(int(resultado[0])+ int(resultado[1])+int(resultado[2]))

# DC X = ((qtdVotosIX * pesoEscala) + (qtdVotosIX * pesoEscala) + (qtdVotosIX * pesoEscala)) \ 3



