args = sys.argv

# further code of the script "add_four_numbers.py"
result = 0
for n in range(1, len(args)):
    result += int(args[n])

print(result)
