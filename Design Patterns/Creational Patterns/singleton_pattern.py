#---------------without singleton-----------------
class Normal:
    def createClass(self):
        pass
a = Normal()
b = Normal()

#-------------with singleton-------------------
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
x = Singleton()
y = Singleton()