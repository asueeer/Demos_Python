input = [   [7],
           [3,8],
          [8,1,0],
         [2,7,4,4],
        [4,5,2,6,5]]
records = dict()
def max_sum(input, start, path_sum):
    if str(start) in records.keys():
        return records[str(start)] + path_sum
    if start[0]==len(input) - 1:
        records[str(start)] = input[start[0]][start[1]]
        return input[start[0]][start[1]] + path_sum

    next_points = [ [start[0] + 1, start[1]], [start[0] + 1, start[1]+ 1]]
    results = []
    for next_point in next_points:
        results.append(max_sum(input, next_point, input[start[0]][start[1]] + path_sum))
    records[str(start)] = max(results) - path_sum
    return max(results)

if __name__ == '__main__':
    print(max_sum(input, [0, 0], 0))
    for k,v in records.items():
        print(k + ":" + str(v))
    print(len(records))