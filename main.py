class Chef:
    def __init__(self,privateVar):
        self.__privateVar=privateVar
    def __privMeth(self):
        print("Hi you can't change me")
    def hello(self):
        self.__privMeth()
        print(self.__privateVar)
c=Chef("avleen")
c.hello()
