def count_runs(flat_data):
    count = 1
    run = 1
    current = flat_data[0]
    for num in flat_data[1:]:
        if current == num:
            count += 1
            if count > 15:
                count = 1
                run += 1
        else:
            count = 1
            current = num
            run += 1
    return run


print(count_runs([3, 4, 4, 8, 8, 8, 3, 3]))
