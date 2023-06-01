def read_file():
    file = open("Laptop.txt","r")
    laptop_id = 1
    my_dict = {}
    for line in file:
        line = line.replace("\n","")
        my_dict[laptop_id] = (line.split(","))
        laptop_id += 1
    file.close()
    return my_dict