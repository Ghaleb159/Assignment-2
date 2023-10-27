from random import randint
#IMPORTING RANDINT FUNCTION FROM RANDOM MODULE

#CLASS DEFINED AS PRODUCT
class product:
    def __init__(self, monthly_product_production):
        self.monthly_product_production = monthly_product_production
    
    inventory_amount = 0 #INVENTORY SET AS 0

    #CLASSMETHOD CHANGES 'INVENTORY_AMOUNT' TO THE MONTHLY INVENTORY AMOUNT
    @classmethod
    def change_inventory_amount(cls, inventory_amount):
        cls.inventory_amount = inventory_amount

    #PRODUCT_QUANTITY_SOLD METHOD CREATES A RANGE USING MONTHLY_PRODUCT_PRODUCTION TO GET A RANDINT BETWEEN 
    # SELF.MINUS_PRODUCT & SELF.ADD_PRODUCT WHICH WOULD BE THE PRODUCT_QUANTITY_SOLD  
    def product_quantity_sold(self, monthly_product_production):
        self.minus_product = monthly_product_production - 10
        self.add_product = monthly_product_production + 10
        self.product_quantity_sold = randint(self.minus_product, self.add_product)
        return self.product_quantity_sold
    
    #IT IS A METHOD WHICH DETERMINES HOW MUCH INVENTORY IS LEFT. IT ADDS THE MONTHLY_PRODUCT_PRODUCTION
    #AND THAN SUBTRACTS THE PRODUCT_QUANTITY_SOLD WHICH WILL RESULT TO BE THE INVENTORY_LEVEL
    @classmethod
    def product_quantity(cls, monthly_product_production, product_quantity_sold):
        cls.inventory_level = cls.inventory_amount + monthly_product_production
        cls.inventory_level = cls.inventory_level - product_quantity_sold
        return cls.inventory_level
    

