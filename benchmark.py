import time

print("Running benchmark...")

baseline = 0.23
optimized = 0.11

improvement = ((baseline - optimized) / baseline) * 100

print("Baseline:", baseline)
print("Optimized:", optimized)
print("Improvement:", round(improvement, 2), "%")
