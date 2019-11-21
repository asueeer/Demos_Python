M = 6
items = [[1,4],[2,6],[3,12],[2,7]] # [x,y] 表示[体积，价值]

def max_value(items,left,sum_V):
    if len(items) == 1:
        if left >= items[0][0]:
            return sum_V + items[0][1]
        else:
            return sum_V

    results = []
    results.append(max_value(items[:-1], left,sum_V))
    if left >= items[-1][0]:
        results.append(max_value(items[:-1], left - items[-1][0], sum_V + items[-1][1]))
    return max(results)

if __name__ == '__main__':
    print(max_value(items, M, 0))