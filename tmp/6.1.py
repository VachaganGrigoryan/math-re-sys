import math

n = int(input("Enter N = "))
lmd = [float(input(f"Enter lambda[{i}] : ")) for i in range(n)]

t = int(input("Enter t = "))

Lh = sum(lmd)

Ph = float(math.e**(-t*Lh))
Th = 1/Lh
Fh = Lh*Ph
# Qh = (1 - Ph)**(n+1)

print('Anxapan achxatanqi havanakanutyuny = %.20f' % Ph)
print('Anxapan ashxatanqi mijin jamanaky = %.10f' % Th)
print('Jamanaki bachxman xtutyun =  %.20f' % Fh)