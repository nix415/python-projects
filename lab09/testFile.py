from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_CarInventoryNode():
    node = CarInventoryNode(Car("Nissan", "Leaf", 2018, 18000))
    assert node.getMake() == "NISSAN"
    assert node.getModel() == "LEAF"
    assert node.getParent() == None
    assert node.getLeft() == None
    assert node.getRight() == None
def test___eq__():
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Nissan", "Leaf", 2018, 18000)
    car3 = Car("Nissan", "Leaf", 2018, 18000)
    car4 = Car("Toyota", "Leaf", 2018, 900)
    assert car1.__eq__(car2) == True
    assert car2.__eq__(car3) == True
    assert car3.__eq__(car4) == False
def test___gt__():
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Nissan", "Leaf", 2018, 18000)
    car3 = Car("Nissan", "Leaf", 2018, 18000)
    car4 = Car("Toyota", "Leaf", 2018, 900)
    assert car1.__gt__(car2) == False

'''
1. write down the expected output on paper
2. run the code
3. compare the actual output to the expected output
'''
def test_inOrder():
    car1 = Car("toyota", "prius", 2022, 25000)
    car2 = Car("Honda", "ODYSSEY", 2009, 30000)
    car3 = Car("Ferrari", "testarossa", 1990, 100000)
    car4 = Car("Chevrolet", "Equinox", 2011, 10000)

    bst1 = CarInventory()
    bst1.addCar(car1)
    bst1.addCar(car2)
    bst1.addCar(car3)
    bst1.addCar(car4)
    assert bst1.inOrder() == \
"""\
Make: CHEVROLET, Model: EQUINOX, Year: 2011, Price: $10000
Make: FERRARI, Model: TESTAROSSA, Year: 1990, Price: $100000
Make: HONDA, Model: ODYSSEY, Year: 2009, Price: $30000
Make: TOYOTA, Model: PRIUS, Year: 2022, Price: $25000
"""



    car1 = Car("toyota", "prius", 2022, 25000)
    car2 = Car("Honda", "ODYSSEY", 2009, 30000)
    car3 = Car("Ferrari", "testarossa", 1990, 100000)
    car4 = Car("ferrari", "monza", 2020, 500000)
    car5 = Car("Chevrolet", "Equinox", 2011, 10000)

    bst = CarInventory()
    bst.addCar(car1)
    bst.addCar(car5)
    bst.addCar(car4)
    bst.addCar(car3)
    bst.addCar(car2)

    car1 = Car("toyota", "prius", 2022, 25000)
    car2 = Car("Honda", "ODYSSEY", 2009, 30000)
    car3 = Car("Ferrari", "testarossa", 1990, 100000)
    car4 = Car("Chevrolet", "Equinox", 2011, 10000)

    bst = CarInventory()
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)

    car1 = Car("toyota", "prius", 2022, 25000)
    car2 = Car("Honda", "ODYSSEY", 2009, 30000)
    car3 = Car("Ferrari", "testarossa", 1990, 100000)
    car4 = Car("Chevrolet", "Equinox", 2011, 10000)

    bst = CarInventory()
    bst.addCar(car4)
    bst.addCar(car3)
    bst.addCar(car2)
    bst.addCar(car1)

    car1 = Car("toyota", "prius", 2022, 25000)
    car2 = Car("Honda", "ODYSSEY", 2009, 30000)
    car3 = Car("Chevrolet", "Equinox", 2011, 10000)
    car4 = Car("Toyota", "Sienna", 2007, 35000)
    car5 = Car("Toyota", "Corolla", 2006, 10000)
    car6 = Car("toyota", "camry", 2007, 11000)
    car7 = Car("TOYOTA", "raV4", 2008, 12000)

    bst = CarInventory()
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    bst.addCar(car7)

    car1 = Car("toyota", "prius", 2022, 25000)
    car2 = Car("Honda", "ODYSSEY", 2009, 30000)
    car3 = Car("Ferrari", "testarossa", 1990, 100000)
    car4 = Car("Chevrolet", "Equinox", 2011, 10000)

    bst = CarInventory()
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)


def test_CarInventory():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5) 

def doesCarExist():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    assert bst.doesCarExist(car1) == True
    assert bst.doesCarExist(car2) == True
    assert bst.doesCarExist(car3) == True
    assert bst.doesCarExist(car4) == True
    assert bst.doesCarExist(car5) == True
    
def test_removeCar3():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
def test_removeCar4():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
def test_removeCar5():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)    
    assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
def test_removeCar6():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)    
    assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""



def test_removeCar7():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.removeCar("BMW", "X5", 2020, 58000)
    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    bst.removeCar("BMW", "X5", 2022, 60000)
    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""


def test_removeCar(): #removes a car with a right child
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.removeCar("BMW", "X5", 2020, 58000)
    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
#removes a node with cars. there is no right child
def test_removeCar():
    bst = CarInventory()    

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.removeCar("BMW", "X5", 2020, 58000)

    assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""



def test_removeCar():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.removeCar("BMW", "X5", 2020, 58000)

    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""





def test_removeCar2():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.removeCar("Tesla", "Model3", 2018, 50000)

    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: BMW, Model: X5, Year: 2020, Price: $58000
Make: AUDI, Model: A3, Year: 2021, Price: $25000
"""







