# ==============================================================================
# Experiment No. 8
# Title: Analysis of Multilevel Memory Hierarchy
# ==============================================================================

def memory_hierarchy():
    n = int(input("Enter number of memory levels (2 or 3): "))
    C, S, H, T = [], [], [], []
    for i in range(n):
        print(f"\nLevel {i + 1}")
        for lst, p in zip((C, S, H, T), ("Cost per bit: ", "Size (bits): ", "Hit rate: ", "Access time (microseconds): ")):
            lst.append(float(input(p)))
    
    cost_avg = sum(c * s for c, s in zip(C, S)) / sum(S)
    time_avg = H[0] * T[0] + (1 - H[0]) * T[1] + ((1 - H[0]) * (1 - H[1]) * T[2] if n == 3 else 0)
    
    print("\nAverage Cost per Bit =", cost_avg, "INR/bit")
    print("Average Access Time =", time_avg, "microseconds")

memory_hierarchy()
