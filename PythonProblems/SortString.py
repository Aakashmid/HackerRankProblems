my_str=input()
def custom_sort_logic(char):
    if char.isalpha() :
        return (-1,char) if char.islower() else (0,char)
    elif char.isdigit():
        return (1,char) if int(char)%2!=0 else (2,char)
    else:
        return  (3,char)

print(''.join(sorted(my_str,key=custom_sort_logic)))