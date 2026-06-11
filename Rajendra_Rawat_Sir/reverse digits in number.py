n = int(input('Enter a number:'))
reversed_num = 0
while n > 0:
       digit = n % 10           # get last digit
       reversed_num = reversed_num * 10 + digit            #shift and add digits
       n = n // 10            # remove last digit
print(reversed_num)