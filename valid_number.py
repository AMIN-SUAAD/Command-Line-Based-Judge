def isNumber(s):
    def is_valid(str):
        e_splitted = str.split('e')
        E_splitted = str.split('E')
        
        if e_splitted.count('')>0 or E_splitted.count('')>0:
            return False

        e_splitted = [string for string in e_splitted if string != ""]
        E_splitted = [string for string in E_splitted if string != ""]


        if len(e_splitted) == 2:
            return is_decimal_or_integer(e_splitted[0]) and is_integer(e_splitted[1])
        elif len(E_splitted) == 2:
            return is_decimal_or_integer(E_splitted[0]) and is_integer(E_splitted[1])
        else:
            return is_decimal_or_integer(str)

    def is_decimal_or_integer(num):
        if len(num) > 1:
            if num[0] == '+' or num[0] == '-':
                num = num[1:]

        if num.count('.') > 1:
            return False
    
    
        splitted = num.split('.')
                    
        
        if splitted.count('') > 1:
            return False

        without_empty_strings = [string for string in splitted if string != ""]

        count = 0

        for i in without_empty_strings:
            if i.isnumeric():
                count = count + 1
        if count == len(without_empty_strings):
            return True
        else:
            return False
    
    def is_integer(num):
        if num[0] == '+' or num[0] == '-':
            num = num[1:]
        if num.isnumeric():
            return True
        else:
            return False
    return(is_valid(s))


for i in range(10):
    print(isNumber(input()))
