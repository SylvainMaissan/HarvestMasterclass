class item:
    def __init__(self, price, x, y, z):
       self.price = price
	self.x = x
	self.y = y
	self.z = z

def calculatePrice(self, amount, discount = false):
    if discount:
	return self.price * amount * 0.90
    return self.price * amount

def calculateShipmentSize(self, amount):
    shipmentSize = self.x * self.y * self.z * amount
    return shipmentSize
