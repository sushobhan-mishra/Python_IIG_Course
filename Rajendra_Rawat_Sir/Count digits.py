n = int(input('Enter a number:'))
count = 0
while n > 0:
       n = n//10      #remove last digit
       count += 1
print(count)       