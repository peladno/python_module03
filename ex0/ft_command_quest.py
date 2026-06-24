import sys

print("=== Command Quest ===")
path, *args = sys.argv
argc = len(sys.argv)
print(f"Program name: {path}")
if argc == 1:
    print("No argument provided!")
else:
    print(f"Arguments received {argc - 1}")
i = 0
for data in args:
    print(f"Argument {i + 1}: {data}")
    i += 1
print(f"Total arguments: {argc}")
