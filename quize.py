def consecutive_zeros(string):
    count = 0
    max_count = 0
    for i in range(len(string)):
        if string[i] == "0":
            count += 1
            if i < len(string) - 1 and string[i + 1] == "0":
                continue
            else:
                if count > max_count:
                    max_count = count
                count = 0

    return max_count

print(consecutive_zeros("1001101000110"))