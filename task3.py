var1 = int(input("number1"))
var2 = int(input("number2"))
if (var1 - var2) < 0:
    result = (-1) * (var1 - var2) / var1 + var2
else:
    result = (var1 - var2) / var1 + var2
print(result)
