def exponent(num,exponent):
    result = 1

    for i in range(0,exponent):
        result *=num

    return result

def reverse_string(str):
    reversed = ""
    index = len(str)
    while(index>0):
        reversed+=str[index-1]
        index-=1

    return reversed

print(exponent(4,3))
print(reverse_string("bruh"))
