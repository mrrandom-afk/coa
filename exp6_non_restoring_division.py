def binary(num, bits):
    return format(num & ((1 << bits) - 1), f'0{bits}b')

Q, M = int(input("Enter Dividend : ")), int(input("Enter Divisor : "))
n = Count = max(Q.bit_length(), M.bit_length())
A = 0

print(f"\nInitial Values\n-----------------------------------------\nA = {binary(A, n)}\nQ = {binary(Q, n)}\nM = {binary(M, n)}\nCount = {Count}")

for i in range(1, n + 1):
    print(f"\nIteration {i}\n-----------------------------------------")
    A = (A << 1) | (Q >> (n - 1))
    Q = (Q << 1) & ((1 << n) - 1)
    print(f"After Shift Left AQ\nA = {binary(A, n)}\nQ = {binary(Q, n)}")
    
    op = '-' if A >= 0 else '+'
    A += -M if A >= 0 else M
    print(f"\nA = A {op} M\nA = {binary(A, n)}")
    
    bit = int(A >= 0)
    Q = (Q | 1) if bit else (Q & ~1)
    print(f"Q0 = {bit}\nUpdated Q = {binary(Q, n)}\nCount = {n - i}")

if A < 0:
    A += M
    print(f"\nFinal Restoration (A = A + M)\nA = {binary(A, n)}")

print(f"\n=========================================\nFinal Result\nQuotient = {binary(Q, n)} = {Q}\nRemainder = {binary(A, n)} = {A}")
