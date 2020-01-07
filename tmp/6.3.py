import math

m = int(input("Enter m = "))
lmd0 = float(input("Enter lambda[0] : "))
t = int(input("Enter t = "))
Qh = 1 - math.e**(-lmd0*t)
Ph = 1 - Qh**(m+1)
P1 = math.e**(-lmd0*t)
Th = 1/lmd0 * sum(1/i for i in range(1,m+1))
T0 = 1/lmd0
Fh = lmd0*(m+1)*math.e**(-lmd0*t)*Qh**m
LMDh = Fh / Ph
Gt = Th/T0
Gpt = Ph/P1

print("Mshtakan pahustavorvac hamakargi`")
print('\tAnxapan ashxatanqi havanakanutyuny = %.20f' % Ph)
print('\tAnxapan ashxatanqi havanakanutyuny P1 = %.20f' % P1)
print('\tAnxapan ashxatanqi mijin jamanaky = %.10f' % Th)
print('\tAnxapan ashxatanqi xapanumneri hachaxakanutyun =  %.20f' % Fh)
print('\tAnxapan ashxatanqi ujgnutyun =  %.20f' % LMDh)

print("\nPahustavorman shnorhiv stacvac shahumnery`")
print('\tYst Ph(t) =  %.20f' % Gpt)
print('\tYst Th =  %.20f' % Gt)
