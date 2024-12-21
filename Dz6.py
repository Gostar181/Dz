

result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0,  8 : 4}

for key, value in data.items():
    try:
        res = divider(int(key), value)
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Error with key={key}, value={value}: {e}")


print("Result:",result)