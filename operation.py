from read import read_file
from datetime import datetime

def purchase_laptop():
    print("Thank you for buying")
    print("\n")
    print("*********************************************************************")
    print("PROVIDE YOUR DETAILS FOR FURTHER USES")
    print("*********************************************************************")
    print("\n")
    name = input("Enter your name :")
    phone= input("Enter your phone number :")
    print("#######################################################################################################")
    print("S.N. \t Name \t\t     Brand \t    Price \t Quantity \t Processor \t Graphic Card")
    print("#######################################################################################################")
    a = 1
    file = open("Laptop.txt","r")
    for line in file:
        print(a, "\t" + line.replace(",","\t"))
        a =a+ 1
    print("#######################################################################################################")  
    file.close()
    print("\n")
    
    valid_id = int(input("Please Provide the ID of the product you want to buy:"))
    print("\n")

    #Valid ID
            
    while valid_id <= 0 or valid_id > len(read_file()):
        print("Please provide a valid Laptop ID !!")
        print("\n")
        valid_id = int(input("Please Provide the ID of the laptop you want to buy:"))
    user_quantity = int(input("Please Provide the number of quantity of the Laptop you want to buy:"))
    print("\n")
        
    
    #Valid Quantity

    my_dict = read_file()
    get_quantity = my_dict[valid_id][3]
    while user_quantity <= 0 :
        print("Dear Admin, the quantity you looking for is not available in our shop. Please look again in the Laptop screen")
        print("\n")
        user_quantity = int(input("Please Provide the number of quantity of the Laptop you want to buy: "))
    print("\n")

    #Update the text file

    my_dict[valid_id][3] = int(my_dict[valid_id][3]) + int(user_quantity)

    file = open("Laptop.txt","w")

    for values in my_dict.values():
        file.write(str(values[0])+"," +str(values[1])+"," +str(values[2])+"," +str(values[3])+"," +str(values[4])+"," +str(values[5]))
        file.write("\n")
    file.close()

    #Purchasing from manufacturer

    product_name = my_dict[valid_id][0]
    brand_name = my_dict[valid_id][1]
    quantity_of_user = user_quantity
    price_of_unit = my_dict[valid_id][2].replace("$","")
    final_price = int(price_of_unit)*int(quantity_of_user)

    purchased_laptops = []
    purchased_laptops.append([product_name,brand_name, quantity_of_user, price_of_unit, final_price])
    final_total = 0
    VAT = 0.13
    final_total = final_total + final_price


    buy_loop = True
    while buy_loop == True:
        buy = input("Do you want to buy more laptops?(y/n):")
        if buy == "y" or buy == "Y":

            #Valid ID
            
            while valid_id <= 0 or valid_id > len(read_file()):
                print("Please provide a valid Laptop ID !!")
                print("\n")
            valid_id = int(input("Please Provide the ID of the laptop you want to buy:"))
            user_quantity = int(input("Please Provide the number of quantity of the Laptop you want to buy:"))
            print("\n")

           
            #Valid Quantity

            my_dict = read_file()
            get_quantity = my_dict[valid_id][3]
            while user_quantity <= 0: 
                print("Dear Admin, the quantity you looking for is not available in our shop. Please look again in the Laptop screen")
                print("\n")
                user_quantity = int(input("Please Provide the number of quantity of the Laptop you want to buy: "))
            print("\n")

            #Update the text file

            my_dict[valid_id][3] = int(my_dict[valid_id][3]) + int(user_quantity)

            file = open("Laptop.txt","w")

            for values in my_dict.values():
                file.write(str(values[0])+"," +str(values[1])+"," +str(values[2])+"," +str(values[3])+"," +str(values[4])+"," +str(values[5]))
                file.write("\n")
            file.close()

            #Purchasing from manufacturer

            product_name = my_dict[valid_id][0]
            brand_name = my_dict[valid_id][1]
            quantity_of_user = user_quantity
            price_of_unit = my_dict[valid_id][2].replace("$","")
            final_price = int(price_of_unit)*int(quantity_of_user)

            final_total = final_total + final_price
            VAT = 0.13 * final_total
            total_with_vat = VAT + final_total
           
            purchased_laptops.append([product_name,brand_name, quantity_of_user, price_of_unit, final_price])
            
        else:
            buy_loop = False

    date_time = datetime.now()
    print("\n")
    print("\t \t \t \t YADAV Laptop Shop")
    print("\n")
    print("\t \t Kamalpokhari, Kathmandu | Phone No: 9824801886 ")
    print("\n")
    print("#########################################################################################")
    print("Laptop Details: ")
    print("#########################################################################################")
    print("Customer Name:" + str(name))
    print("Phone Number: " + str(phone))
    print("Date and Time: " + str(date_time))
    print("##########################################################################################")
    print("\n")
    print("Purchase Details are:")
    print("###########################################################################################################")
    print("Product Name \t\t Brand \t\t Total Quantity \t Unit Price \t\t Total")
    print("###########################################################################################################")
    for i in purchased_laptops:
        print(i[0],"\t",i[1],"\t",i[2],"\t\t\t",i[3],"\t\t","$",i[4])
    print("###########################################################################################################")
    
    print("Vat Amount:",  VAT)
    print("Grand Total:" + str(total_with_vat))
    print("Note: Vat Amount added to grand total")

    return name,phone,date_time,purchased_laptops,VAT,final_total, total_with_vat







    

    # today_date_and_time = datetime.now
def sale_laptop():
    print("Thank you for selling")
    print("\n")
    print("*********************************************************************")
    print("visiters detail for further use")
    print("*********************************************************************")
    print("\n")
    name = input("Enter your name :")
    phone = input("Enter your phone :")
    print("*********************************************************************************************************")
    print("S.N. \t Name \t\t      Brand \t   Price \t Quantity \t Processor \t Graphic Card")
    print("*********************************************************************************************************")
    a = 1
    file = open("Laptop.txt","r")
    for line in file:
        print(a, "\t" + line.replace(",","\t"))
        a =a+ 1
    print("*********************************************************************************************************")  
    file.close()
    print("\n")
    
    valid_id = int(input("Please Provide the ID of the product you want to sell:"))
    print("\n")

    #Valid ID

    while valid_id <= 0 or valid_id > len(read_file()):
        print("Please provide a valid Laptop ID !!")
        print("\n")
        valid_id = int(input("Please Provide the ID of the laptop you want to sell:"))
    user_quantity = int(input("Please Provide the number of quantity of the laptop you want to sell:"))
    print("\n")

    #Valid Quantity

    my_dict = read_file()
    get_quantity = my_dict[valid_id][3]
    while user_quantity <= 0 or user_quantity > int(get_quantity):
        print("Dear Admin, the quantity you looking for is not available in our shop. Please look again in the Laptop screen")
        print("\n")
        user_quantity = int(input("Please Provide the number of quantity of the Laptop you want to sell: "))
    print("\n")

    #Update the text file

    my_dict[valid_id][3] = int(my_dict[valid_id][3]) - int(user_quantity)

    file = open("Laptop.txt","w")

    for values in my_dict.values():
        file.write(str(values[0])+"," +str(values[1])+"," +str(values[2])+"," +str(values[3])+"," +str(values[4])+"," +str(values[5]))
        file.write("\n")
    file.close()

    #getting user purchased items

    product_name = my_dict[valid_id][0]
    brand_name = my_dict[valid_id][1]
    quantity_of_user = user_quantity
    price_of_unit = my_dict[valid_id][2]
    price_of_item = my_dict[valid_id][2].replace("$",'')
    final_price = int(price_of_item)*int(quantity_of_user)

    purchased_laptops = []
    purchased_laptops.append([product_name,brand_name, quantity_of_user, price_of_item, final_price])
    final_total = 0
    final_total = final_total + final_price

    sale_loop = True
    while sale_loop == True:
        continue_sale = input("Do you want to buy more laptops? (y/n) ").lower()
        if continue_sale == "y":
            valid_id = int(input("Please Provide the ID of the product you want to sell:"))
            print("\n")

            #Valid ID

            while valid_id <= 0 or valid_id > len(read_file()):
                print("Please provide a valid Laptop ID !!")
                print("\n")
                valid_id = int(input("Please Provide the ID of the laptop you want to sell:"))
            user_quantity = int(input("Please Provide the number of quantity of the laptop you want to sell:"))
            print("\n")

            #Valid Quantity

            my_dict = read_file()
            get_quantity = my_dict[valid_id][3]
            while user_quantity <= 0 or user_quantity > int(get_quantity):
                print("Dear Admin, the quantity you looking for is not available in our shop. Please look again in the Laptop screen")
                print("\n")
                user_quantity = int(input("Please Provide the number of quantity of the Laptop you want to sell: "))
            print("\n")

            #Update the text file

            my_dict[valid_id][3] = int(my_dict[valid_id][3]) - int(user_quantity)

            file = open("Laptop.txt","w")

            for values in my_dict.values():
                file.write(str(values[0])+"," +str(values[1])+"," +str(values[2])+"," +str(values[3])+"," +str(values[4])+"," +str(values[5]))
                file.write("\n")
            file.close()

            #getting user purchased items

            product_name = my_dict[valid_id][0]
            brand_name = my_dict[valid_id][1]
            quantity_of_user = user_quantity
            price_of_unit = my_dict[valid_id][2]
            price_of_item = my_dict[valid_id][2].replace("$",'')
            final_price = int(price_of_item)*int(quantity_of_user)

            purchased_laptops.append([product_name,brand_name, quantity_of_user, price_of_item, final_price])
            final_total = final_total + final_price
        else:
            sale_loop = False

    date_time = datetime.now()
    cost_of_shipping = input("Dear Customer do you want your laptop to be shipped?(Y/N)")

    print("\n")
    print("\t \t \t \t  YADAV Laptop Shop")
    print("\n")
    print("\t \t Kamalpokhari, Kathmandu | Phone No: 9824801886 ")
    print("****************************************************************************************")
    print("\n")
    print("Laptop Details: ")
    print("*****************")
    print("Customer Name:" + str(name))
    print("Phone Number: " + str(phone))
    print("Date and Time: " + str(date_time))
    print("****************************************************************************************")
    print("\n")
    print("Purchase Details are:")
    print("************************************************************************************************************")
    print("Product Name \t\t Brand \t\t Total Quantity \t Unit Price \t\t Total")
    print("************************************************************************************************************")
    for i in purchased_laptops:
        print(i[0],"\t",i[1],"\t",i[2],"\t\t\t",i[3],"\t\t","$",i[4])
    print("************************************************************************************************************")

    if cost_of_shipping == "Y" or cost_of_shipping == "y":
        total = 0
        cost_of_shipping = 500
        for i in purchased_laptops:
            total += int(i[4])
        final_total = total + cost_of_shipping
        print("Shipping Cost:", cost_of_shipping)
        print("Grand Total:" + str(final_total))
        print("Note: Shipping Cost added to grand total")
    else:
        total = 0
        cost_of_shipping = 0
        for i in purchased_laptops:
            total += int(i[4])
        final_total = total + cost_of_shipping
        print("Grand Total:" + str(final_total))
    
    return name,phone,date_time,purchased_laptops,cost_of_shipping,final_total
