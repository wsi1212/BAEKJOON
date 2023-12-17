my_list = [[10,20],[20,30],[30,40],[40,50],[50,60]]

for i in range(len(my_list)):
    for j in range(i, len(my_list) - i):
        element = my_list[j]
        print(f"Index {j}: Element = {element}")