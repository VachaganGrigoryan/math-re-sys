import math

from const.constants import METHOD
from const.methods import SystemProperty
from functools import reduce


class Systems:

    def __init__(self, data, time):
        self._T = list(range(0, time[0] + 1, time[1]))
        self.inData = data
        self.time = time
        self.systems = []
        self.calculator()
        print(self.systems)

    def add(self, system):
        self.systems.append(system)

    def remove(self, system):
        self.systems.remove(system)

    def clear(self):
        self.systems = []

    @property
    def get_T(self):
        return self._T

    @property
    def get_Pc(self):
        Pc = [system.probability for system in self.systems]
        print(Pc)
        return reduce(lambda prod, elm: prod*elm, Pc)

    @property
    def get_Dc(self):
        pass

    def calculator(self):

        for data in self.inData:
            type_one = data["typeOne"]
            type_two_three = data["typeTwoAndThree"]
            system = METHOD.get_by_id(data["system"])
            m, n, is_same = data["row"], data["col"], data["isSame"]
            value, time = data["values"], self.time

            if type_one:
                self.add(BackupSystem(type_two_three)(system, value, m, n, is_same, time))
            else:
                self.add(NotBackupSystem(system, value, time))



def BackupSystem(type_two_three):
    SWITCH = {
        "00": ReplacementByElements, # Փոխարինումով Ըստ էլեմենտների
        "01": ReplacementByWhole, # Փոխարինումով Ընդհանուր
        "10": PermanentByElements, # Մշտական Ըստ էլեմենտների
        "11": PermanentByWhole # Մշտական Ընդհանուր
    }
    return SWITCH.get(type_two_three)



class ReplacementByElements(SystemProperty):

    def __init__(self, system, value, m, n, is_same, time):
        super().__init__()
        self.system = system
        self.value = value
        self.time = time

        self._probability = sum((value[0][0] * time[0])**j / math.factorial(j) for j in range(m+1)) * self.system.P(value[0][0], time[0]) if is_same \
            else sum(((value[0][j]*time[0])**j * system.P(value[0][j], time[0])) / math.factorial(j) for j in range(m+1))


class ReplacementByWhole(SystemProperty):

    def __init__(self, system, value, m, n, is_same, time):
        super().__init__()
        self.system = system
        self.value = value
        self.time = time

        self._probability = sum([reduce(lambda prod, elm: prod * elm, [((val*time[0])**j * system.P(val, time[0])) / math.factorial(j) for val in  list(zip(*value))[0] ]) for j in range(m+1)]) if is_same \
            else sum([reduce(lambda prod, elm: prod * elm, [((val*time[0])**j * system.P(val, time[0])) / math.factorial(j) for val in item]) for j, item in enumerate(zip(*value))])


class PermanentByElements(SystemProperty):

    def __init__(self, system, value, m, n, is_same, time):
        super().__init__()
        self.system = system
        self.value = value
        self.time = time

        self._probability = 1 - pow(1-self.system.P(self.value[0][0], time[0]), m+1) if is_same \
            else reduce(lambda prob, el: prob * el, [1 - self.system.P(val, time[0]) for val in value[0]])


class PermanentByWhole(SystemProperty):

    def __init__(self, system, value, m, n, is_same, time):
        super().__init__()
        self.system = system
        self.value = value
        self.time = time

        self._probability = 1 - pow(1 - reduce(lambda prod, elm: prod*elm, [self.system.P(val, time[0]) for val in list(zip(*value))[0]]), m+1) if is_same\
            else reduce(lambda prod, elm: prod*elm, [1 - reduce(lambda prod, elm: prod*elm, [self.system.P(val, time[0]) for val in item]) for item in zip(*value)])



class NotBackupSystem(SystemProperty):

    def __init__(self, system, value, time):
        super().__init__()
        self.system = system
        self.value = value
        self.time = time

        self._probability = self.system.P(value[0][0], self.time[0])


if __name__ == '__main__':
    # values = [
    #     {'system': [0, 'Ցուցչային'], 'row': 1, 'col': 1, 'typeOne': [1, 'Պահուստավորված'], 'typeTwo': [1, 'Մշտական'],
    #      'typeThree': [0, 'Ըստ տարրերի'], 'isSame': [True, 'Արժեքները նույնն են'], 'values': [[0.0005]]},
    #     {'system': [0, 'Ցուցչային'], 'row': 1, 'col': 1, 'typeOne': [1, 'Պահուստավորված'], 'typeTwo': [1, 'Մշտական'],
    #      'typeThree': [0, 'Ըստ տարրերի'], 'isSame': [True, 'Արժեքները նույնն են'], 'values': [[0.0008]]},
    #     {'system': [0, 'Ցուցչային'], 'row': 0, 'col': 1, 'typeOne': [0, 'Չպահուստավորված'], 'typeTwo': None,
    #      'typeThree': None, 'isSame': [None], 'values': [[0.0006]]}]

    # values = [{'system': 0, 'row': 1, 'col': 1, 'typeOne': 1, 'typeTwoAndThree': '10', 'isSame': True,
    #            'values': [[0.0005]]},
    #           {'system': 0, 'row': 1, 'col': 1, 'typeOne': 1, 'typeTwoAndThree': '10', 'isSame': True,
    #            'values': [[0.0006]]},
    #           {'system': 0, 'row': 0, 'col': 1, 'typeOne': 0, 'typeTwoAndThree': None, 'isSame': None,
    #            'values': [[0.0008]]}]

    # values = [{'system': 0, 'row': 1, 'col': 2, 'typeOne': 1, 'typeTwoAndThree': '11', 'isSame': True, 'values': [[0.0003], [0.0008]]},
    #           {'system': 0, 'row': 0, 'col': 1, 'typeOne': 0, 'typeTwoAndThree': None, 'isSame': None, 'values': [[0.0005]]}]

    values = [{'system': 0, 'row': 1, 'col': 2, 'typeOne': 1, 'typeTwoAndThree': '11', 'isSame': False, 'values': [[0.003, 0.001], [0.002, 0.001]]},
              {'system': 0, 'row': 2, 'col': 1, 'typeOne': 1, 'typeTwoAndThree': '00', 'isSame': True, 'values': [[0.002]]}]

    time = [1000, 100]

    sys = Systems(values, time)

    print(sys.get_Pc)

