# encapsulation in python
class Sakthivel:
    def init(self):
        self.city = 'Cheyyar'
        self._bank = 'CUB'
        self.__atmPin = 1234

    def display(self):
        print(self.__atmPin)


sakthi = Sakthivel()
sakthi.display()
print(sakthi.city)
print(sakthi._bank)
print(sakthi.__atmpin)
