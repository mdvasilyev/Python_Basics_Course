# iterative both index and item

data = [1, 2, -3, -4]
for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0
print(data)