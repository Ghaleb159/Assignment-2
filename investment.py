from application import product


#CREATED A FUNCTION
def investment():
    print('__________________________________________________________________')
    print('__________________________________________________________________')
    your_name = input('\nWHAT IS YOUR NAME USER: ') #ASKS USER FOR THEIR NAME
    print('__________________________________________________________________')
    print('__________________________________________________________________')
    print(f'\nWELCOME {your_name}, THANK YOU FOR USING MY PROGRAM')
    print('__________________________________________________________________')
    print('__________________________________________________________________')

    product_name = str(input('\nPLEASE ENTER THE PRODUCT NAME:  ')) #ASKS USER FOR PRODUCT NAME
    print('__________________________________________________________________')
    print('__________________________________________________________________')
    print(f'\nPRODUCT NAME IS {product_name}')
    print('__________________________________________________________________')
    print('__________________________________________________________________')


    while True: #AS LONG AS IT IS TRUE, IT WILL GO THROUGH THE WHILE LOOP
        try:
            product_code = int(input("\nPLEASE ENTER PRODUCT CODE (100 - 1000):  ")) #ASKS USER FOR PRODUCT CODE BETWEEN 100 - 1000
            if 100 <= product_code <= 1000:
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                print(f"\nPRODUCT CODE IS {product_code}")
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                break
            else:
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                print("\nINVALID ENTRY, PLEASE ENTER PRODUCT CODE AGAIN (100 - 1000):") #IF USER ENTERS A CODE THAT IS LESS THEN 100 OR MORE THEN 1000
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                continue
        except ValueError:
            print('__________________________________________________________________')
            print('__________________________________________________________________')
            print("\nINVALID ENTRY. PLEASE ENTER PRODUCT CODE AGAIN (100 - 1000):") #REPEAT THE CODE IF USER ENTERS ANYTHING OTHER THEN AN INTEGER
            print('__________________________________________________________________')
            print('__________________________________________________________________')
            continue

    while True: #AS LONG AS IT IS TRUE, IT WILL GO THROUGH THE WHILE LOOP
        try:
            product_manufacture_cost = float(input('\nPLEASE ENTER PRODUCT MANUFACTURE COST:  ')) #ASKS USER FOR A FLOAT NUMBER FOR MANUFACTURE COST 
            if product_manufacture_cost > 0:
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                print(f'\nPRODUCT MANUFACTURE COST IS {product_manufacture_cost}')
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                break
            else:
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                print('\nPLEASE ENTER THE MANUFACTURE COST AGAIN (GREATER THAN ZERO):  ') #IF COST IS LESS THEN 0 THEN IT REPEATS 
                print('__________________________________________________________________')
                print('__________________________________________________________________')
        except ValueError:
            print('__________________________________________________________________')
            print('__________________________________________________________________')
            print('\nINVALID ENTRY, ENTER MANUFACTURE COST AGAIN!!!') #IF USER ENTERS ANYTHING OTHER THEN A NUMBER IT REPEATS
            print('__________________________________________________________________')
            print('__________________________________________________________________')

    while True: #AS LONG AS IT IS TRUE, IT WILL GO THROUGH THE WHILE LOOP
        try:
            monthly_units_manufactured = int(input('\nPLEASE ENTER ESTIMATED MONTHLY PRODUCTION:  ')) #ASKS USER FOR AN INTEGER NUMBER FOR ESTIMATED MONTHLY PRODUCTION
            if monthly_units_manufactured >= 0:
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                print(f'\nESTIMATED MONTHLY PRODUCTION IS {monthly_units_manufactured}')
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                break
            else:
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                print('\nINVALID ENTRY, PLEASE ENTER ESTIMATED MONTHLY PRODUCTION AGAIN:  ') #IF LESS THEN 0 IT REPEATS
                print('__________________________________________________________________')
                print('__________________________________________________________________')
        except ValueError:
            print('__________________________________________________________________')
            print('__________________________________________________________________')
            print('\nINVALID ENTRY, PLEASE ENTER ESTIMATED MONTHLY PRODUCTION!!!')
            print('__________________________________________________________________')
            print('__________________________________________________________________')


    while True: #AS LONG AS IT IS TRUE, IT WILL GO THROUGH THE WHILE LOOP
        try:
            product_sale_price = float(input('\nPLEASE ENTER PRODUCT PRICE:  ')) #ASKS USER TO ENTER A FLOAT NUMBER FOR PRODUCT PRICE
            if product_sale_price > 0:
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                print(f'\nPRODUCT PRICE IS {product_sale_price}')
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                break
            else:
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                print('\nINVALID ENTRY, PLEASE ENTER PRODUCT PRICE (GREATER THAN ZERO)  ') #MUST BE GREATER THEN 0 OR IT WILL REPEAT
                print('__________________________________________________________________')
                print('__________________________________________________________________')
        except ValueError: #IF USER ENTERS ANYTHING OTHER THEN A NUMBER, IT REPEATS
            print('__________________________________________________________________')
            print('__________________________________________________________________')
            print('\nINVALID ENTRY, PLEASE ENTER PRODUCT PRICE!!!')
            print('__________________________________________________________________')
            print('__________________________________________________________________')
            
    while True: #AS LONG AS IT IS TRUE, IT WILL GO THROUGH THE WHILE LOOP
        try:
            inventory_level = int(input('\nPLEASE ENTER THE INVENTORY LEVEL:  ')) #ASKS USER TO ENTER AN INTEGER FOR THE INVENTORY LEVEL
            if inventory_level > 0:
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                print(f'\nINVENTORY LEVEL IS {inventory_level}')
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                break
            else:
                print('__________________________________________________________________')
                print('__________________________________________________________________')
                print('\nINVALID ENTRY, PLEASE ENTER THE INVENTORY LEVEL:  ') #IF INVENTORY LEVEL IS 0 OR LESS, IT REPEATS
                print('__________________________________________________________________')
                print('__________________________________________________________________')
        except ValueError: #IF USER ENTERS ANYTHING OTHER THEN A NUMBER, IT REPEATS
            print('__________________________________________________________________')
            print('__________________________________________________________________')
            print('\nINVALID ENTRY, PLEASE ENTER THE INVENTORY LEVEL!!!')
            print('__________________________________________________________________')
            print('__________________________________________________________________')
            
    #LISTS ALL USER INPUTS
    user_result = f''' 
 _________________________________________________________________
|   ______________________________________________________________
|  |                                                           
|  |                           USER ENTERED
|  |                     
|  |                        USER NAME: {your_name}
|  |                     
|  |                     PRODUCT NAME: {product_name}  
|  |
|  |                     PRODUCT CODE: {product_code}   
|  |
|  |                 MANUFACTURE COST: {product_manufacture_cost}
|  |
|  |               MONTHLY PRODUCTION: {monthly_units_manufactured} 
|  |
|  |                    PRODUCT PRICE: {product_sale_price}        
|  |
|  |                  INVENTORY LEVEL: {inventory_level}                       
|  |                                                           
|  |                                                           
|  |______________________________________________________________
|_________________________________________________________________
    '''
    print(user_result)





    #PROCESSING OF SALES FOR MONTH_1
    month_1 = product(monthly_units_manufactured)
    print('\n                          MONTH 1:')
    print(f'\n               MONTHLY PRODUCTION: {month_1.monthly_product_production}')
    print(f'\n                       UNITS SOLD: {month_1.product_quantity_sold(monthly_units_manufactured)}')

    product.change_inventory_amount(inventory_level)

    product.product_quantity(monthly_units_manufactured, month_1.product_quantity_sold)
    print(f'\n                        INVENTORY: {month_1.inventory_level}')

    print('\n_________________________________________________________________')

    #PROCESSING OF SALES FOR MONTH_2
    month_2 = product(monthly_units_manufactured)
    print('\n                          MONTH 2:')
    print(f'\n               MONTHLY PRODUCTION: {month_2.monthly_product_production}')
    print(f'\n                       UNITS SOLD: {month_2.product_quantity_sold(monthly_units_manufactured)}')

    product.change_inventory_amount(inventory_level)

    product.product_quantity(monthly_units_manufactured, month_2.product_quantity_sold)
    print(f'\n                        INVENTORY: {month_2.inventory_level}')

    print('\n_________________________________________________________________')

    #PROCESSING OF SALES FOR MONTH_3
    month_3 = product(monthly_units_manufactured)
    print('\n                          MONTH 3:')
    print(f'\n               MONTHLY PRODUCTION: {month_3.monthly_product_production}')
    print(f'\n                       UNITS SOLD: {month_3.product_quantity_sold(monthly_units_manufactured)}')

    product.change_inventory_amount(inventory_level)

    product.product_quantity(monthly_units_manufactured, month_3.product_quantity_sold)
    print(f'\n                        INVENTORY: {month_3.inventory_level}')

    print('\n_________________________________________________________________')

    #PROCESSING OF SALES FOR MONTH_4
    month_4 = product(monthly_units_manufactured)
    print('\n                          MONTH 4:')
    print(f'\n              nMONTHLY PRODUCTION: {month_4.monthly_product_production}')
    print(f'\n                       UNITS SOLD: {month_4.product_quantity_sold(monthly_units_manufactured)}')

    product.change_inventory_amount(inventory_level)

    product.product_quantity(monthly_units_manufactured, month_4.product_quantity_sold)
    print(f'\n                        INVENTORY: {month_4.inventory_level}')

    print('\n_________________________________________________________________')

    #PROCESSING OF SALES FOR MONTH_5
    month_5 = product(monthly_units_manufactured)
    print('\n                          MONTH 5:')
    print(f'\n               MONTHLY PRODUCTION: {month_5.monthly_product_production}')
    print(f'\n                       UNITS SOLD: {month_5.product_quantity_sold(monthly_units_manufactured)}')

    product.change_inventory_amount(inventory_level)

    product.product_quantity(monthly_units_manufactured, month_5.product_quantity_sold)
    print(f'\n                        INVENTORY: {month_5.inventory_level}')

    print('\n_________________________________________________________________')

    #PROCESSING OF SALES FOR MONTH_6
    month_6 = product(monthly_units_manufactured)
    print('\n                          MONTH 6:')
    print(f'\n               MONTHLY PRODUCTION: {month_6.monthly_product_production}')
    print(f'\n                       UNITS SOLD: {month_6.product_quantity_sold(monthly_units_manufactured)}')

    product.change_inventory_amount(inventory_level)

    product.product_quantity(monthly_units_manufactured, month_6.product_quantity_sold)
    print(f'\n                        INVENTORY: {month_6.inventory_level}')

    print('\n_________________________________________________________________')

    #PROCESSING OF SALES FOR MONTH_7
    month_7 = product(monthly_units_manufactured)
    print('\n                          MONTH 7:')
    print(f'\n               MONTHLY PRODUCTION: {month_7.monthly_product_production}')
    print(f'\n                       UNITS SOLD: {month_7.product_quantity_sold(monthly_units_manufactured)}')

    product.change_inventory_amount(inventory_level)

    product.product_quantity(monthly_units_manufactured, month_7.product_quantity_sold)
    print(f'\n                        INVENTORY: {month_7.inventory_level}')

    print('\n_________________________________________________________________')

    #PROCESSING OF SALES FOR MONTH_8
    month_8 = product(monthly_units_manufactured)
    print('\n                          MONTH 8:')
    print(f'\n               MONTHLY PRODUCTION: {month_8.monthly_product_production}')
    print(f'\n                       UNITS SOLD: {month_8.product_quantity_sold(monthly_units_manufactured)}')

    product.change_inventory_amount(inventory_level)

    product.product_quantity(monthly_units_manufactured, month_8.product_quantity_sold)
    print(f'\n                        INVENTORY: {month_8.inventory_level}')

    print('\n_________________________________________________________________')

    #PROCESSING OF SALES FOR MONTH_9
    month_9 = product(monthly_units_manufactured)
    print('\n                          MONTH 9:')
    print(f'\n               MONTHLY PRODUCTION: {month_9.monthly_product_production}')
    print(f'\n                       UNITS SOLD: {month_9.product_quantity_sold(monthly_units_manufactured)}')

    product.change_inventory_amount(inventory_level)

    product.product_quantity(monthly_units_manufactured, month_9.product_quantity_sold)
    print(f'\n                        INVENTORY: {month_9.inventory_level}')

    print('\n_________________________________________________________________')

    #PROCESSING OF SALES FOR MONTH_10
    month_10 = product(monthly_units_manufactured)
    print('\n                         MONTH 10:')
    print(f'\n               MONTHLY PRODUCTION: {month_10.monthly_product_production}')
    print(f'\n                       UNITS SOLD: {month_10.product_quantity_sold(monthly_units_manufactured)}')

    product.change_inventory_amount(inventory_level)

    product.product_quantity(monthly_units_manufactured, month_10.product_quantity_sold)
    print(f'\n                        INVENTORY: {month_10.inventory_level}')

    print('\n_________________________________________________________________')

    #PROCESSING OF SALES FOR MONTH_11
    month_11 = product(monthly_units_manufactured)
    print('\n                          MONTH 11:')
    print(f'\n                MONTHLY PRODUCTION: {month_11.monthly_product_production}')
    print(f'\n                        UNITS SOLD: {month_11.product_quantity_sold(monthly_units_manufactured)}')

    product.change_inventory_amount(inventory_level)

    product.product_quantity(monthly_units_manufactured, month_11.product_quantity_sold)
    print(f'\n                         INVENTORY: {month_11.inventory_level}')

    print('\n_________________________________________________________________')

    #PROCESSING OF SALES FOR MONTH_12
    month_12 = product(monthly_units_manufactured)
    print('\n                          MONTH 12:')
    print(f'\n                MONTHLY PRODUCTION: {month_12.monthly_product_production}')
    print(f'\n                        UNITS SOLD: {month_12.product_quantity_sold(monthly_units_manufactured)}')

    product.change_inventory_amount(inventory_level)

    product.product_quantity(monthly_units_manufactured, month_12.product_quantity_sold)
    print(f'\n                         INVENTORY: {month_12.inventory_level}')

    print('\n ________________________________________________________________')

    #CALCULATES THE TOTAL SOLD PRODUCT ANNUALLY
    total_sold_product = int(month_1.product_quantity_sold + month_2.product_quantity_sold + month_3.product_quantity_sold + month_4.product_quantity_sold + month_5.product_quantity_sold + month_6.product_quantity_sold + 
    month_7.product_quantity_sold + month_8.product_quantity_sold + month_9.product_quantity_sold + month_10.product_quantity_sold + month_11.product_quantity_sold + month_12.product_quantity_sold)

    #CALCULATES ANNUAL MANUFACTURED PRODUCTS WITHIN THE 12 MONTHS
    total_annual_manufactured_product = int(monthly_units_manufactured * 12)

    #CALCULATES THE NET PROFIT FOR THE YEAR, [(Total Units Sold * Sale Price) - (Total Units Manufactured * Manufacture Cost)]
    net_profit = float((total_sold_product * product_sale_price) - (total_annual_manufactured_product * product_manufacture_cost))

    print(f'|\n|                        NET PROFIT: ${net_profit}')

    print('|\n|________________________________________________________________')

investment()

#FREE PALESTINE
free_palestine = '''
                 
 ____________________________________________________________________________________________________________________
|                                                                                                                    |
|                     *             *                                                                                |
|                    ***           ***              __________    ________      ________   ________                  |
|                   *****         *****            |             |        \    |          |                          |
|                  *******       *******           |             |         |   |          |                          |
|                 *********     *********          |_______      |________/    |_____     |_____                     |
|                ***********   ***********         |             |   \         |          |                          |
|                ************ ************         |             |    \        |          |                          |
|                 ***********************          |             |     \       |________  |________                  |
|                  *********************           ________________________________________________                  |
|                   *******************           |*                                               |                 |
|                    *****************            |***                                             |                 |
|                     ***************             |******   _______________________________________|                 |
|                      *************              |*********                                       |                 |
|                       ***********               |************      FROM THE RIVER TO THE SEA     |                 |
|                        *********                |***************                                 |                 |
|                          *****                  |************       FALESTINE WILL BE FREE       |                 |
|                           ***                   |*********_______________________________________|                 |
|                            *                    |******                                          |                 |
|                                                 |***                                             |                 |
|                                                 |*_______________________________________________|                 |
|____________________________________________________________________________________________________________________|
|   |                                                                                                            |   | 
||||| *                *                *           __________________________           *                 *     |||||
|   |        *                  *              *   |         INFANT           |   *               *              |   | 
||||| *                *                *          |__________________________|          *                 *     |||||
|   |                                                  / /    ____   \ \                                         |   |
|||||                                                 / /    /. . \   \ \                                        |||||
|   |                                                / /    |  _  |    \ \                                       |   |
|||||                                               / /_____ \___/ _____\ \                                      |||||
|   |                                              |_______|       |_______|                                     |   |
|||||                                                      |  FREE |                                             |||||
|   |                                                      |  GAZA |                                             |   |
|||||                                                      |       |                                             |||||
|   |                                                      |   _   |                                             |   |
|||||                                                      |  | |  |                                             |||||
|   |                                                      |  | |  |                                             |   |
|||||______________________________________________________|__|_|__|_____________________________________________|||||
''' 

print(free_palestine)

