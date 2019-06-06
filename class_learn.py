


class Father:
    def eat(self):
        print("I can eat")
class Mother:
    def walk(self):
        print('Walk like mother')

class Son(Father,Mother):  #类的继承
    #类的重载
    def eat(self):
        print("I like eat")
    def walk(self):
        print("walk like son")


littleInty = Son()
littleInty.eat()
littleInty.walk()
