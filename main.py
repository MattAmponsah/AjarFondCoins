Temp1 =float(input("Enter temperature:"))

unit = input("Enter unit in F/f or C/c:")

tempc = float((Temp1 - 32.0) * 5.0 / 9.0)

tempf = float(Temp1 * 9.0 / 5.0 + 32.0)

if unit == 'F' or unit == 'f':print(f"{Temp1}° in Fahrenheit is equivalent to {tempc}° Celsius.")

elif unit == 'C' or unit == 'c':print(f"{Temp1}° in Celsius is equivalent to {tempf}° Fahrenheit.")

else:print (f"Invalid unit({unit}).")
