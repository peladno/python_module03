import sys

print("=== Command Quest ===")
path, *arg = sys.argv
arg_len = len(sys.argv) 
print(f"Program name: {path}")
if arg_len == 1:
    print("No argument provided!")
else:
    print(f"Arguments received {arg_len - 1}")
for i in range(len(arg)):
    print(f"Argument {i + 1}: {arg[i]}")
print(f"Total arguments: {arg_len}")
