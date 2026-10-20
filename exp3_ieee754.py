# ==============================================================================
# Experiment No. 3
# Title: IEEE 754 Floating Point Representation (Single Precision)
# ==============================================================================

number = float(input("Enter a decimal number: "))
sign, number = (0, number) if number >= 0 else (1, -number)
print("Sign Bit =", sign)

integer, frac = int(number), number - int(number)
binary_integer = bin(integer)[2:]
print("Binary Integer =", binary_integer)

binary_fraction = ""
for _ in range(10):
    frac *= 2
    binary_fraction += "1" if frac >= 1 else "0"
    if frac >= 1:
        frac -= 1
print("Binary Fraction =", binary_fraction)

print("Binary Number =", binary_integer + "." + binary_fraction)

exponent = len(binary_integer) - 1
mantissa = binary_integer[1:] + binary_fraction
print("Normalized Form = 1." + mantissa + " x 2^", exponent)

biased_exponent = exponent + 127
print("Biased Exponent =", biased_exponent)
binary_exponent = bin(biased_exponent)[2:]
print("Exponent in Binary =", binary_exponent)

mantissa = mantissa.ljust(23, '0')[:23]
print("Mantissa =", mantissa)

print("\nIEEE 754 Representation")
print(str(sign) + binary_exponent + mantissa)
