# ==============================================================================
# Experiment No. 4
# Title: Booth's Multiplication Algorithm for Signed Binary Multiplication
# ==============================================================================

def binary(num, bits):
    return format(num & ((1 << bits) - 1), f'0{bits}b')

def booth(multiplicand, multiplier, bits=4):
    A, Q, M, Q_1 = 0, multiplier, multiplicand, 0
    print(f"\nInitial Values\nA = {binary(A, bits)}\nQ = {binary(Q, bits)}\nM = {binary(M, bits)}\nQ-1 = {Q_1}")
    print("\nIteration\tA\t\tQ\tQ-1")
    for i in range(bits):
        if (Q & 1) != Q_1:
            A += -M if (Q & 1) else M
        comb = ((A << (bits + 1)) | (Q << 1) | Q_1) >> 1
        Q_1, Q, A = comb & 1, (comb >> 1) & ((1 << bits) - 1), comb >> (bits + 1)
        print(i + 1, "\t\t", binary(A, bits), "\t", binary(Q, bits), "\t", Q_1)
    product = (A << bits) | Q
    print(f"\nBinary Product : {binary(product, bits * 2)}\nDecimal Product : {multiplicand * multiplier}")

m = int(input("Enter Multiplicand : "))
q = int(input("Enter Multiplier : "))
booth(m, q, 4)
