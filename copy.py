original = [1, 2, 3, 4]
copy = original[:]  # This makes a copy

print("Original list:", original)
print("Copied list:  ", copy)

copy[0] = 100

print("After changing copy:")
print("Original list:", original) 
print("Copied list:  ", copy)     