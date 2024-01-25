from Car import Car
class CarInventoryNode(Car):
    
    def __init__(self, car):
        super().__init__(car.make, car.model, car.year, car.price)
        self.parent = None
        self.left = None
        self.right = None
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.cars = [car]


    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getParent(self):
        return self.parent
    def setParent(self, parent):
        self.parent = parent
    def getLeft(self):
        return self.left
    def setLeft(self, left):
        self.left = left
    def getRight(self):
        return self.right
    def setRight(self, right):
        self.right = right

    def __str__(self):
        ret = ''
        for car in self.cars:
            ret += str(car) + '\n'
        return ret

    def replaceNodeData(self, car):
        self.make = car.make
        self.model = car.model
        self.year = car.year
        self.price = car.price
        self.cars = [car]
        if self.getLeft() is not None:
            self.left.parent = self
        if self.getRight() is not None:
            self.right.parent = self

            