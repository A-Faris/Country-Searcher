def cleaned_counts(data: list[int]) -> list[int]:
    clean = [data[0]]
    for num in data[1:]:
        if num >= clean[-1]:
            clean.append(num)
        else:
            clean.append(num+1)

    return clean


cleaned_counts([2, 1, 2])
