from decimal import Decimal 

print("Enter a float to Round Up ?")
myfloat = Decimal(raw_input())
output = Decimal(myfloat.quantize(decimal.Decimal('.01'),rounding=decimal.ROUND_HALF_UP))
print(output)
