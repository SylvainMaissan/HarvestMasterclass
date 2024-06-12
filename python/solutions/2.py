class item:
    def __init__(self, price, lenght, width, heigth):
        self.price = price
        self.length = length
        self.width = width
        self.heigth = heigth

    def calculatePrice(self, amount, discount = 1):
        return self.price * amount * discount
    
    def calculateShipmentSize(self, amount):
        shipmentSize = self.length * self.width * self.heigth * amount
        return shipmentSize
