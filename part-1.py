from random import randint

class product:
    def __init__(self, monthly_product_production):
        self.monthly_product_production = monthly_product_production
    
    inventory_amount = 0
   
    @classmethod
    def change_inventory_amount(cls, stock_amount):
        cls.inventory_amount = stock_amount

    
    def product_quantity_sold(self, monthly_product_production):
        self.minus_product = monthly_product_production - 10
        self.add_product = monthly_product_production + 10
        self.product_quantity_sold = randint(self.minus_product, self.add_product)
        return self.product_quantity_sold
    
    @classmethod
    def product_quantity(cls, monthly_product_production, product_quantity_sold):
        cls.inventory_level = cls.inventory_amount + monthly_product_production
        cls.inventory_level = cls.inventory_level - product_quantity_sold
        return cls.inventory_level
    
        
'''
(inputs)
Product Code (e.g., an integer from 100 to 1000) 
Product Name (e.g. Laser Printer)
Product Sale Price (e.g., a real number greater than zero)
Product Manufacture Cost (e.g., a real number greater than zero)
Stock Level (an integer number greater than 0)
Estimated Monthly Units Manufactured (e.g. an integer greater than or equal to 0)
'''

your_name = input('\nWHAT IS YOUR NAME USER: ')
print(f'WELCOME {your_name}, THANK YOU FOR USING MY PROGRAM')

product_name = str(input('\nPLEASE ENTER THE PRODUCT NAME:  '))
print(f'\nPRODUCT NAME IS {product_name}')

while True:
    try:
        product_code = int(input("\nPLEASE ENTER PRODUCT CODE:  "))
        if 100 <= product_code <= 1000:
            print(f"\nPRODUCT CODE IS {product_code}")
            break
        else:
            print("\nINVALID ENTRY, PLEASE ENTER PRODUCT CODE AGAIN (100 - 1000):")
            continue
    except ValueError:
        print("\nINVALID ENTRY. PLEASE ENTER PRODUCT CODE AGAIN (100 - 1000):")
        continue

while True:
    try:
        product_manufacture_cost = float(input('\nPLEASE ENTER PRODUCT MANUFACTURE COST:  '))
        if product_manufacture_cost > 0:
             print(f'\nPRODUCT MANUFACTURE COST IS {product_manufacture_cost}')
             break
        else:
            product_manufacture_cost = float(input('\nPLEASE ENTER THE MANUFACTURE COST AGAIN (GREATER THAN ZERO):  '))
    except ValueError:
        print('\nINVALID ENTRY, ENTER MANUFACTURE COST AGAIN!!!')

while True:
    try:
        monthly_units_manufactured = int(input('\nPLEASE ENTER ESTIMATED MONTHLY PRODUCTION:  '))
        if monthly_units_manufactured > 0:
             print(f'\nESTIMATED MONTHLY PRODUCTION IS {monthly_units_manufactured}')
             break
        else:
            monthly_units_manufactured = int(input('\nINVALID ENTRY, PLEASE ENTER ESTIMATED MONTHLY PRODUCTION AGAIN:  '))
    except ValueError:
        print('\nINVALID ENTRY, PLEASE ENTER ESTIMATED MONTHLY PRODUCTION!!!')


while True:
    try:
        product_sale_price = float(input('\nPLEASE ENTER PRODUCT PRICE:  '))
        if product_sale_price > 0:
            print(f'\nPRODUCT PRICE IS {product_sale_price}')
            break
        else:
            product_sale_price = float(input('\nINVALID ENTRY, PLEASE ENTER PRODUCT PRICE:  '))
    except ValueError:
        print('\nINVALID ENTRY, PLEASE ENTER PRODUCT PRICE!!!')
        
while True:
    try:
        inventory_level = int(input('\nPLEASE ENTER THE INVENTORY LEVEL:  '))
        if inventory_level > 0:
            print(f'\nINVENTORY LEVEL IS {inventory_level}')
            break
        else:
            inventory_level = int(input('\nINVALID ENTRY, PLEASE ENTER THE INVENTORY LEVEL:  '))
    except ValueError:
        print('\nINVALID ENTRY, PLEASE ENTER THE INVENTORY LEVEL!!!')

result = f'''
 ________________________________________________________________
|                                                           
|                                                           
|                     PRODUCT NAME: {product_name}  
|
|                     PRODUCT CODE: {product_code}   
|
|                 MANUFACTURE COST: {product_manufacture_cost}
|
|               MONTHLY PRODUCTION: {monthly_units_manufactured} 
|
|                    PRODUCT PRICE: {product_sale_price}        
|
|                  INVENTORY LEVEL: {inventory_level}                       
|                                                           
|                                                           
|________________________________________________________________
'''
print(result)






month_1 = product(monthly_units_manufactured)
print('\n                          MONTH 1:')
print(f'\n               MONTHLY PRODUCTION: {month_1.monthly_product_production}')
print(f'\n                       UNITS SOLD: {month_1.product_quantity_sold(monthly_units_manufactured)}')

product.change_inventory_amount(inventory_level)

product.product_quantity(monthly_units_manufactured, month_1.product_quantity_sold)
print(f'\n                        INVENTORY: {month_1.inventory_level}')

print('\n_________________________________________________________________')

month_2 = product(monthly_units_manufactured)
print('\n                          MONTH 2:')
print(f'\n               MONTHLY PRODUCTION: {month_2.monthly_product_production}')
print(f'\n                       UNITS SOLD: {month_2.product_quantity_sold(monthly_units_manufactured)}')

product.change_inventory_amount(inventory_level)

product.product_quantity(monthly_units_manufactured, month_2.product_quantity_sold)
print(f'\n                        INVENTORY: {month_2.inventory_level}')

print('\n_________________________________________________________________')

month_3 = product(monthly_units_manufactured)
print('\n                          MONTH 3:')
print(f'\n               MONTHLY PRODUCTION: {month_3.monthly_product_production}')
print(f'\n                       UNITS SOLD: {month_3.product_quantity_sold(monthly_units_manufactured)}')

product.change_inventory_amount(inventory_level)

product.product_quantity(monthly_units_manufactured, month_3.product_quantity_sold)
print(f'\n                        INVENTORY: {month_3.inventory_level}')

print('\n_________________________________________________________________')

month_4 = product(monthly_units_manufactured)
print('\n                          MONTH 4:')
print(f'\n              nMONTHLY PRODUCTION: {month_4.monthly_product_production}')
print(f'\n                       UNITS SOLD: {month_4.product_quantity_sold(monthly_units_manufactured)}')

product.change_inventory_amount(inventory_level)

product.product_quantity(monthly_units_manufactured, month_4.product_quantity_sold)
print(f'\n                        INVENTORY: {month_4.inventory_level}')

print('\n_________________________________________________________________')

month_5 = product(monthly_units_manufactured)
print('\n                          MONTH 5:')
print(f'\n               MONTHLY PRODUCTION: {month_5.monthly_product_production}')
print(f'\n                       UNITS SOLD: {month_5.product_quantity_sold(monthly_units_manufactured)}')

product.change_inventory_amount(inventory_level)

product.product_quantity(monthly_units_manufactured, month_5.product_quantity_sold)
print(f'\n                        INVENTORY: {month_5.inventory_level}')

print('\n_________________________________________________________________')

month_6 = product(monthly_units_manufactured)
print('\n                          MONTH 6:')
print(f'\n               MONTHLY PRODUCTION: {month_6.monthly_product_production}')
print(f'\n                       UNITS SOLD: {month_6.product_quantity_sold(monthly_units_manufactured)}')

product.change_inventory_amount(inventory_level)

product.product_quantity(monthly_units_manufactured, month_6.product_quantity_sold)
print(f'\n                        INVENTORY: {month_6.inventory_level}')

print('\n_________________________________________________________________')

month_7 = product(monthly_units_manufactured)
print('\n                          MONTH 7:')
print(f'\n               MONTHLY PRODUCTION: {month_7.monthly_product_production}')
print(f'\n                       UNITS SOLD: {month_7.product_quantity_sold(monthly_units_manufactured)}')

product.change_inventory_amount(inventory_level)

product.product_quantity(monthly_units_manufactured, month_7.product_quantity_sold)
print(f'\n                        INVENTORY: {month_7.inventory_level}')

print('\n_________________________________________________________________')

month_8 = product(monthly_units_manufactured)
print('\n                          MONTH 8:')
print(f'\n               MONTHLY PRODUCTION: {month_8.monthly_product_production}')
print(f'\n                       UNITS SOLD: {month_8.product_quantity_sold(monthly_units_manufactured)}')

product.change_inventory_amount(inventory_level)

product.product_quantity(monthly_units_manufactured, month_8.product_quantity_sold)
print(f'\n                        INVENTORY: {month_8.inventory_level}')

print('\n_________________________________________________________________')

month_9 = product(monthly_units_manufactured)
print('\n                          MONTH 9:')
print(f'\n               MONTHLY PRODUCTION: {month_9.monthly_product_production}')
print(f'\n                       UNITS SOLD: {month_9.product_quantity_sold(monthly_units_manufactured)}')

product.change_inventory_amount(inventory_level)

product.product_quantity(monthly_units_manufactured, month_9.product_quantity_sold)
print(f'\n                        INVENTORY: {month_9.inventory_level}')

print('\n_________________________________________________________________')

month_10 = product(monthly_units_manufactured)
print('\n                         MONTH 10:')
print(f'\n               MONTHLY PRODUCTION: {month_10.monthly_product_production}')
print(f'\n                       UNITS SOLD: {month_10.product_quantity_sold(monthly_units_manufactured)}')

product.change_inventory_amount(inventory_level)

product.product_quantity(monthly_units_manufactured, month_10.product_quantity_sold)
print(f'\n                        INVENTORY: {month_10.inventory_level}')

print('\n_________________________________________________________________')

month_11 = product(monthly_units_manufactured)
print('\n                          MONTH 11:')
print(f'\n                MONTHLY PRODUCTION: {month_11.monthly_product_production}')
print(f'\n                        UNITS SOLD: {month_11.product_quantity_sold(monthly_units_manufactured)}')

product.change_inventory_amount(inventory_level)

product.product_quantity(monthly_units_manufactured, month_11.product_quantity_sold)
print(f'\n                         INVENTORY: {month_11.inventory_level}')

print('\n_________________________________________________________________')

month_12 = product(monthly_units_manufactured)
print('\n                          MONTH 12:')
print(f'\n                MONTHLY PRODUCTION: {month_12.monthly_product_production}')
print(f'\n                        UNITS SOLD: {month_12.product_quantity_sold(monthly_units_manufactured)}')

product.change_inventory_amount(inventory_level)

product.product_quantity(monthly_units_manufactured, month_12.product_quantity_sold)
print(f'\n                         INVENTORY: {month_12.inventory_level}')

print('\n _________________________________________________________________')

total_sold_product = month_1.product_quantity_sold + month_2.product_quantity_sold + month_3.product_quantity_sold + month_4.product_quantity_sold + month_5.product_quantity_sold + month_6.product_quantity_sold + month_7.product_quantity_sold + month_8.product_quantity_sold + month_9.product_quantity_sold + month_10.product_quantity_sold + month_11.product_quantity_sold + month_12.product_quantity_sold

total_annual_manufactured_product = monthly_units_manufactured * 12

net_profit = (total_sold_product * product_sale_price) - (total_annual_manufactured_product * product_manufacture_cost)

print(f'|\n|                        NET PROFIT: ${net_profit}')

print('|\n|_________________________________________________________________')

free_palestine = '''
                 

                     *             *
                    ***           ***              __________    ________      ________   ________
                   *****         *****            |             |        \    |          |
                  *******       *******           |             |         |   |          |
                 *********     *********          |_______      |________/    |_____     |_____
                ***********   ***********         |             |   \         |          |
                ************ ************         |             |    \        |          |
                 ***********************          |             |     \       |________  |________
                  *********************           ________________________________________________
                   *******************           |*                                               |
                    *****************            |***                                             |
                     ***************             |******__________________________________________|
                      *************              |*********                                       |
                       ***********               |************      FROM THE RIVER TO THE SEA     |
                        *********                |***************                                 |
                          *****                  |************       FALESTINE WILL BE FREE       |
                           ***                   |*********_______________________________________|
                            *                    |******                                          |
                                                 |***                                             |
                                                 |*_______________________________________________|



                            ''' 

print(free_palestine)
 