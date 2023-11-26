
L = [10,20,30,20,10,50,60,40,80,50,40]

L_sans_doublons = []

for i in L:
    if i not in L_sans_doublons:
        L_sans_doublons.append(i)

print(L_sans_doublons)