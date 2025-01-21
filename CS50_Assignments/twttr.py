s = input("Input: ")

print("Output: ", end="")
for ss in s:
    if not ss.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(ss , end="")
print()   