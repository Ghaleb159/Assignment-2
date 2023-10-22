'''
(inputs)
Product Code (e.g., an integer from 100 to 1000) 
Product Name (e.g. Laser Printer)
Product Sale Price (e.g., a real number greater than zero)
Product Manufacture Cost (e.g., a real number greater than zero)
Stock Level (an integer number greater than 0)
Estimated Monthly Units Manufactured (e.g. an integer greater than or equal to 0)
'''

product_name = str(input('\nPLEASE ENTER THE PRODUCT NAME:  '))
print(f'\nPRODUCT NAME IS {product_name}')

while True:
    try:
        product_code = int(input("\nPLEASE ENTER PRODUCT CODE:  "))
        if 100 <= product_code <= 1000:
            print(f"\nPRODUCT CODE IS {product_code}")
            break
        else:
            product_code = int(input("\nINVALID ENTRY, PLEASE ENTER PRODUCT CODE AGAIN (100 - 1000):"))
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
        stock_level = int(input('\nPLEASE ENTER THE STOCK LEVEL:  '))
        if stock_level > 0:
            print(f'\nSTOCK LEVEL IS {stock_level}')
            break
        else:
            stock_level = int(input('\nINVALID ENTRY, PLEASE ENTER THE STOCK LEVEL:  '))
    except ValueError:
        print('\nINVALID ENTRY, PLEASE ENTER THE STOCK LEVEL!!!')







