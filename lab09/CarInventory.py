from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:

    def __init__(self):
        self.root = None

    def addCar(self, car): 
        if self.root:
            self._addCar(car, self.root)
        else:
            self.root = CarInventoryNode(car)

    def _addCar(self, newnode, currentNode):
        currentCar = currentNode.cars[0] 
        if newnode.make == currentCar.make and newnode.model == currentCar.model:
            currentNode.cars.append(newnode)
            
        elif newnode.make > currentCar.make or (newnode.make == currentCar.make and newnode.model > currentCar.model):
            if currentNode.right:
                self._addCar(newnode, currentNode.right)
            else:
                newCar = CarInventoryNode(newnode)
                newCar.setParent(currentNode)
                currentNode.setRight(newCar)
        
        elif newnode.make < currentCar.make or (newnode.make == currentCar.make and newnode.model < currentCar.model):
            if currentNode.left:
                self._addCar(newnode, currentNode.left)
            else:
                newCar = CarInventoryNode(newnode)
                newCar.setParent(currentNode)
                currentNode.setLeft(newCar)

    def doesCarExist(self, car):
        if self.root:
            for c in self.root.cars:
                if c.__eq__(car):
                    return True
        return self._doesCarExist(car, self.root)

        
    def _doesCarExist(self, newnode, currentNode):
        if currentNode.left:
            for c in currentNode.left.cars:
                if c.__eq__(newnode):
                    return True
                
        if currentNode.right:
            for c in currentNode.right.cars:
                if c.__eq__(newnode):
                    return True
                
        if currentNode.left and currentNode.right:
            return self._doesCarExist(newnode, currentNode.left) or self._doesCarExist(newnode, currentNode.right)
        elif currentNode.left:
            return self._doesCarExist(newnode, currentNode.left)
        elif currentNode.right:
            return self._doesCarExist(newnode, currentNode.right)
        else:
            return False


    def inOrder(self):
        return self._inOrder(self.root)
    
    def _inOrder(self, currentNode):    
        ret = ''
        if currentNode != None:
            ret += self._inOrder(currentNode.left)
            ret += str(currentNode)
            ret += self._inOrder(currentNode.right)
        return ret

    def preOrder(self):
        return self._preOrder(self.root)
    
    def _preOrder(self, currentNode):
        ret = ''
        if currentNode != None:
            ret += str(currentNode)
            ret += self._preOrder(currentNode.left)
            ret += self._preOrder(currentNode.right)
        return ret
    
    def postOrder(self):
        return self._postOrder(self.root)
    
    def _postOrder(self, currentNode):
        ret = ''
        if currentNode != None:
            
            ret += self._postOrder(currentNode.left)
            ret += self._postOrder(currentNode.right)
            ret += str(currentNode)
        return ret
        
    def getBestCar(self, make, model):
        return self._getBestCar(make, model, self.root)

    def _getBestCar(self, make, model, currentNode): 
        current = self.root
        temp = Car(make, model, 0, 0)
        
        while current != None:
            if current.make == make.upper() and current.model == model.upper():
                bestCar = current.cars[0]
                for car in current.cars:
                    if car.__gt__(bestCar):
                        bestCar = car
                return bestCar

            else:
                if temp.__gt__(current.cars[0]):
                    current = current.right
                else: 
                    current = current.left    
    def getWorstCar(self, make, model):
        return self._getWorstCar(make, model)
    def _getWorstCar(self, make, model):
        current = self.root
        temp = Car(make, model, 0, 0)
        
        while current != None:
            if current.make == make.upper() and current.model == model.upper():
                worstCar = current.cars[0]
                for car in current.cars:
                    if car.__lt__(worstCar):
                        worstCar = car
                return worstCar

            else:
                if temp.__gt__(current.cars[0]):
                    current = current.right
                else:
                    current = current.left
            
        
    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)
    
    def _getTotalInventoryPrice(self, currentNode):
        if currentNode is None:
            return 0
        else:
            total = 0
            for i in currentNode.cars:
                total += i.price
            return total + self._getTotalInventoryPrice(currentNode.left) + self._getTotalInventoryPrice(currentNode.right)

    def get(self, make, model):
        if self.root:
            return self._get(make, model, self.root)
        else:
            return None

    def _get(self, make, model, currentNode):
        if currentNode is None:
            return None
        elif currentNode.make == make.upper() and currentNode.model == model.upper():   
            return currentNode
        elif make.upper() < currentNode.make or (make.upper() == currentNode.make and model.upper() < currentNode.model):
            return self._get(make, model, currentNode.left)
        else:
            return self._get(make, model, currentNode.right)

    def getSuccessor(self, make, model):
        currentNode = self.get(make, model)
        if currentNode == None:
            return None
        else:
            if currentNode.right != None:
                return self._getSuccessor(currentNode.right)
            else:
                parent = currentNode.parent
                while parent != None:
                    if currentNode != parent.right:
                        break
                    currentNode = parent
                    parent = parent.parent
                return parent

    def _getSuccessor(self, currentNode):
        if currentNode.left != None:
            return self._getSuccessor(currentNode.left)
        else:
            return currentNode

    def spliceOut(self, currentNode):
        if currentNode.right is None and currentNode.left is None:
            if currentNode.parent.left == currentNode:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None
        elif currentNode.right != None or currentNode.left != None:
            if currentNode.right:
                if currentNode.parent.left == currentNode:
                    currentNode.parent.left = currentNode.right
                else:
                    currentNode.parent.right = currentNode.right
                currentNode.right.parent = currentNode.parent

    def removeCar(self, make, model, year, price):   
        if self.root is None:
            return False
        make = make.upper() 
        model = model.upper()
        car = Car(make, model, year, price)
        if self.root == None:
            return False
        if self.doesCarExist(car) == False:
            return False
        
        if self.root.left is None and self.root.right is None:
            for car_ in self.root.cars:
                if car_ == car:
                    self.root.cars.remove(car_)
                    break
            if len(self.root.cars) == 0:
                self.root = None
            return True

        elif self.root.left != None or self.root.right != None:
            currentNode = self.get(make, model)
            if currentNode:
                for car_ in currentNode.cars:
                    if car_ == car:
                        currentNode.cars.remove(car_)
                        break
                if len(currentNode.cars) == 0:
                    self._removeCar(make, model, year, price, currentNode)
                    return True
                else:
                    return False
        else:
            return False
        return True


    def _removeCar(self, make, model, year, price, currentNode):

        if currentNode.left is None and currentNode.right is None:
            if currentNode == currentNode.parent.left:
                currentNode.parent.left = None
                
            elif currentNode == currentNode.parent.right:
                currentNode.parent.right = None
            else: 
                currentnode = None
                        
        elif currentNode.left != None and currentNode.right != None:
            succ = self.getSuccessor(currentNode.make, currentNode.model)
            self.spliceOut(succ)
            if len(currentNode.cars) > 0:
                currentNode.cars[0] = succ.cars[0]
            else:
                currentNode.cars.append(succ.cars[0])
            
            return True
            succ = self.getSuccessor(currentNode.make, currentNode.model)
            self.spliceOut(succ)
            currentNode.cars[0] = succ.cars[0]
            
            return True
            
        else:  
            if currentNode.left:
                if currentNode.parent:
                    if currentNode.parent.left == currentNode:
                        currentNode.left.parent = currentNode.parent
                        currentNode.parent.left = currentNode.left
                    elif currentNode.parent.right == currentNode:
                        currentNode.left.parent = currentNode.parent
                        currentNode.parent.right = currentNode.left
                else:
                    currentNode.make = currentNode.left.make
                    currentNode.model = currentNode.left.model
                    currentNode.cars = currentNode.left.cars
                    if currentNode.left.left:
                        currentNode.left = currentNode.left.left
                    elif currentNode.left.right:
                        currentNode.left = currentNode.left.right
                    else:
                        currentNode.left = None
            else:
                if currentNode.parent:
                    if currentNode.parent.left == currentNode:
                        currentNode.right.parent = currentNode.parent
                        currentNode.parent.left = currentNode.right
                    elif currentNode.parent.right == currentNode:
                        currentNode.right.parent = currentNode.parent
                        currentNode.parent.right = currentNode.right
                else:
                    currentNode.make = currentNode.right.make
                    currentNode.model = currentNode.right.model
                    currentNode.cars = currentNode.right.cars
                    if currentNode.right.left:
                        currentNode.right = currentNode.right.left
                    elif currentNode.right.right:
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.right = None