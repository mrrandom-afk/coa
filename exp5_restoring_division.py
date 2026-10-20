
A, Q, M = 0, int(input("Enter Dividend : ")), int(input("Enter Divisor : "))
n = Count = max(Q.bit_length(), M.bit_length())

print(f"\nInitial Values\nA = {A}\nQ = {Q}\nM = {M}\nCount = {Count}")

while Count > 0:
    A = (A << 1) | (Q >> (n - 1))
    Q = (Q << 1) & ((1 << n) - 1)
    print(f"\nAfter Shift Left\nA = {A}\nQ = {Q}\nAfter A = A - M\nA = {A - M}")
    A -= M
    if A < 0:
        A += M
        print("Restore A\nQ0 = 0")
        Q &= ~1
    else:
        print("Q0 = 1")
        Q |= 1
    Count -= 1
    print(f"A = {A}\nQ = {Q}\nCount = {Count}")

print(f"\nFinal Result\nQuotient = {Q}\nRemainder = {A}")
