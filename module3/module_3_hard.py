def calculate_structure_sum(data):
    sum = 0
    if isinstance(data, int):
        sum += data
    if isinstance(data, str):
        sum += len(data)
    if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
        for item in data:
            sum += calculate_structure_sum(item)
    if isinstance(data, dict):
        for key, item in data.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(item)
    return sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)