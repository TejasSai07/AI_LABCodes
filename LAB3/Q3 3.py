def maze(adList, visit, curr, goal, path):
    if curr == goal:
        path.append(curr)
        return path
    if curr in visit:
        return path
    visit.append(curr)
    path.append(curr)
    for x in adList[curr]:
        path = maze(adList, visit, x, goal, path)
        if goal in path:
            return path
    return path

if __name__ == '__main__':
    vertices = 20
    adList = [[], [2, 6], [1, 3], [2, 8], [5], [4, 10], [1, 11], [8], [3, 7], [10, 14], [5, 9, 15], [6, 12], [11, 17], [14], [9, 13, 19], [10, 20], [17], [12, 16, 18], [17, 19], [14, 18], [15]]
    visit = []
    path = maze(adList, visit, 2, 5, [])
    print(path)