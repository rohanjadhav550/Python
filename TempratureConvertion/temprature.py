
convertion = input("""Select the convertion option
* C
* F
""")

value = int(input("Enter the value: "))

if convertion == "C":
    formula = (value * 9/5) + 32
    print(formula)
else:
    formula = (value - 32) * 5/9
    print(formula)


