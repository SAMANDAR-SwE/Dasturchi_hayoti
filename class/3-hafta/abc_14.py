from abc import ABC, abstractmethod

class Hayvon(ABC):
    def __init__(self, ism):
        self.ism = ism

    @abstractmethod
    def ovoz(self):
        pass

class It(Hayvon):
    def ovoz(self):
        return "Vov"

class Baliq(Hayvon):
    def ovoz(self):
        return "..."
    

print(It("Rex").ovoz())
