class Object:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.type = None
        self.m = 0
        self.id = 0

class System:
    def __init__(self):
        self.arr_of_obj = []
        self.stat = 0
        id = 0
    def Tick():
        pass
    def append(self, obj):
        obj.id = self.id
        self.id += 1
        self.arr_of_obj.append(obj)


class Star(Object):
    def __init__(self):
        super().__init__()
        self.type = "Star"

class Ship(Object):
    def __init__(self):
        super().__init__()
        setf.type = "Ship"

class Planet(Object):
    def __init__(self):
        super().__init__()
        self.type = "Planet"
