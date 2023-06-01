from operation import *
from write import *

print("\n")
print("#####################################################################################################")
print("***************************** Welcome to YADAV Laptop Shop*************************************")
print("######################################################################################################")
print("\t \t \t Address: Kamalpokhari, Kathmandu | Contact: 9824801886")
print("######################################################################################################")
print("\n")

continueLoop = True
while continueLoop == True:
    print("###################################################################################################################################################")
    print("\n")
    print("# ||||||||||||||||||||||||||| select any option for further  process |||||||||||||||||||||||||| #")
    print("###################################################################################################")
    print("#                                                                                                 #")
    print("#                           Press 1 to sale                                                       #")
    print("#                                                                                                 #")
    print("#                           Press 2 to buy from manufacture.                                      #")
    print("#                                                                                                 #")
    print("#                           Press 3 to Exit from the system.                                      #")
    print("#                                                                                                 #")
    print("###################################################################################################")
    print("\n")
    user_input = 0
    try:
        user_input = int(input("Press your desire extension number (1,2,3):"))
        print("\n")
        Option = False
    except:
         print("Please input valid input 1,2,3 only")

    if user_input == 1:
        #write_sold(*sale_laptop())
         name,phone,date_time,purchased_laptops,cost_of_shipping,final_total = sale_laptop()
         write_sold(name,phone,date_time,purchased_laptops,cost_of_shipping,final_total)
          
                      
    elif user_input == 2:
        name,phone,date_time,purchased_laptops,VAT,final_total, total_with_vat = purchase_laptop()
        write_purchase(name,phone,date_time,purchased_laptops,VAT,final_total, total_with_vat)

        
    elif user_input == 3:
        continueLoop = False
        print("Thank's for visiting")
    else:
        print("Enter correct option")
