import math

m = int(input("Enter m = "))
lmd0 = float(input("Enter lambda[0] : "))
t = int(input("Enter t = "))

Gph = sum(((lmd0 * t)**i)/math.factorial(i) for i in range(m))
Gth = m + 1
Gfh = ((lmd0 * t)**m)/math.factorial(m)

Ph = float((math.e**(-lmd0*t))*Gph)
Ph1 = float((math.e**(-lmd0*t)))
Th = (m+1)/lmd0
Th0 = 1/lmd0
Fh = (lmd0**(m+1) * t**m * math.e**(-lmd0*t)) / math.factorial(m)
LMDh = (lmd0**(m+1) * t**m) / (math.factorial(m) * Gph)

print(" Poxarinumov pahustavorvac hamakargi`")

print('\tAnxapan achxatanqi havanakanutyuny = %.20f' % Ph)
print('\tArajin tari anxapan achxatanqi havanakanutyuny = %.20f' % Ph1)
print('\tAnxapan ashxatanqi mijin jamanaky = %.10f' % Th)
print('\tArajin tari anxapan ashxatanqi mijin jamanaky = %.10f' % Th0)
print('\tAnxapan ashxatanqi xapanumneri hachaxakanutyun =  %.20f' % Fh)
print('\tAnxapan ashxatanqi ujgunutyun =  %.20f' % LMDh)

print("\nPahustavorman shnorhiv stacvac shahumnery`")
print('\tYst Ph(t) =  %.20f' % Gph)
print('\tYst Th =  %.20f' % Gth)
print('\tYst Fh =  %.20f' % Gfh)
