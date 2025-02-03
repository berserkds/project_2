def main(data: list, limit: int) -> int:
    remains = []
    total = 0
    for number in data:
        if number == limit:
            total += 1
        else:
            remains.append(number)
    remains.sort()
    left_pointer = 0
    right_pointer = len(remains) - 1
    while left_pointer <= right_pointer:
        summ = remains[left_pointer] + remains[right_pointer]
        if summ == limit or summ < limit:
            total += 1
            left_pointer += 1
            right_pointer -= 1
        else:
            total += 1
            right_pointer -= 1
    return total


if __name__ == '__main__':
    mas_of_rob = list(map(int, input().split()))
    limit_mas = int(input())
    result = main(mas_of_rob, limit_mas)
    print(result)
