import re

def split_digits(num):
  return [int(d) for d in str(num)]

archivo = open("sourcefile.txt", mode="r")
array = []
sum=0
for line in archivo:
    match = re.findall(r"\d+", line)
    if len(match) == 1:
        output = match[0] * 2
    else:
        output = match[0] + match[-1]
    digits = split_digits(output)
    num = str(digits[0])+''+str(digits[len(digits)-1])
    number = int(num)
    sum += number

print(sum)
    