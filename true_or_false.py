is_valid = input('enter t for true f for false ')
if is_valid == 't':
    is_valid = True
    for even in range(1,100,2):
        print(even)
elif is_valid =='f':
    is_valid =False
    for odd in range(1,100,3):
        print(odd)




