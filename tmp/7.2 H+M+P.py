import math

n = int(input("Enter n : "))
subs = int(input("Enter subs : "))

EH = []

for i in range(subs):
    print(f"For {i+1} subsystem")
    # m = int(input("Enter m (qanaky): "))
    EH.append([int(input("Enter m (qanaky): ")), input("Enter hamakargi type P kam M kam H : "), {'myu':float(input("Enter myu : ")), 'lmd':float(input("Enter lmd : "))}])
    # for j in range(m):
    #     EH[i].append({'myu':float(input("Enter myu : ")), 'lmd':float(input("Enter lmd : "))})


print(EH)
Kph = 1
for i in range(subs):
    m = EH[i][0]
    tp = EH[i][1]
    d = EH[i][2]

    if tp in ["M", "H"]:
        ro = d['lmd']/d['myu']
    elif tp == "P":
        ro = d['myu']/d['lmd']

    Kph *=  sum(ro**j for j in range(m))/sum(ro**j for j in range(m+1))
print("Kph : ", Kph)
