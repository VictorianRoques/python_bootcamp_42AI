import sys
if (len(sys.argv) != 3):
    print("ERROR Invalid numbers of arguments")
    sys.exit()
if sys.argv[1].isdigit() == 0 or sys.argv[2].isdigit() == 0:
    print("Intput Error: only numbers")
    sys.exit()
x = int(sys.argv[1])
y = int(sys.argv[2])
print(f"Sum:        {x + y}")
print(f"Diffrence:  {x - y}")
print(f"Product:    {x * y}")
if y == 0:
    print(f"Quotient:   ERROR (div by zero)")
    print(f"Remainder: ERROR (modulo by zero)")
else:
    print(f"Quotient:  {x / y}")
    print(f"Remainder: {x % y}")