# 132812177
def delivery(data: list, limit: int) -> int:
    sorted_data: list = sorted(data)
    total: int = 0
    light: int = 0
    heavy: int = len(data) - 1
    while light <= heavy:
        summ = sorted_data[light] + sorted_data[heavy]
        if (summ == limit or summ < limit):
            light += 1
        total += 1
        heavy -= 1
    return total


if __name__ == '__main__':
    mas_of_rob = [int(number) for number in input().split()]
    limit_mas = int(input())
    result = delivery(mas_of_rob, limit_mas)
    print(result)
