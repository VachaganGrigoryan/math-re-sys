
class NonRecoverableBackup:

    def __init__(self):
        self._systems = []

    @property
    def systems(self):
        return self._systems
    
    @systems.deleter
    def systems(self):
        self._systems = []

    def add(self, system):
        self._systems.append(system)

    def remove(self, system):
        self._systems.remove(system)



    
class System:
    
    def __init__(self, lmd, myu, _function):
        self.lmd = lmd
        self.myu = myu
        self._function = eval(f'{_function}(self)')

    def all_by_replacement(self): # Ընդհանուր փոխարինումով
        return 

    def all_by_permanent(self): # Ընդհանուր մշտական
        pass

    def еlement_by_replacement(self): # Ըստ տարրերի փոխարինումով
        pass
    
    def еlement_by_permanent(self): # Ըստ տարրերի մշտական
        pass

# Kph = 1
# for i in range(subs):
#     m = EH[i][0]
#     tp = EH[i][1]
#     d = EH[i][2]
#
#     if tp in ["M", "H"]:
#         ro = d['lmd']/d['myu']
#     elif tp == "P":
#         ro = d['myu']/d['lmd']
#
#     Kph *=  sum(ro**j for j in range(m))/sum(ro**j for j in range(m+1))
# print("Kph : ", Kph)