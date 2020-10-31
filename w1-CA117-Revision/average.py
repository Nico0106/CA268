def above_average(numbers):
    above = []
    average = sum(numbers) / len(numbers)
    [above.append(num) for num in numbers if num > average]
    return above
