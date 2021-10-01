import sys


def openFile(fileName):
    items = []

    try:
        file = open(fileName, "r+")
        for line in file:

            line = line.split(",")
            if line == ["cookie", "timestamp\n"]:
                continue

            line[1] = line[1][:10]
            items.append(line)

        file.close()

    except ValueError:
        raise "error: couldn't open the provided log file"

    return items


def buildCounter(fileName):
    dic = {}

    items = openFile(fileName)

    for cookie, time in items:
        if time not in dic:
            dic[time] = {}

        if cookie not in dic[time]:
            dic[time][cookie] = 0

        dic[time][cookie] += 1

    return dic


def getMostActive(date, dic):
    if date not in dic:
        return []

    chunk = dic[date]
    arr = [[key, chunk[key]] for key in chunk]

    arr.sort(key=lambda x: x[1])

    ans = []
    while arr:
        val = arr.pop()

        if not ans:
            ans.append(val)
            continue

        #if no more duplicate counts, break early
        if val[1] != ans[-1][1]:
            break

        ans.append(val)

    return [cookie for cookie, _ in ans]


if __name__ == '__main__':
    args = sys.argv
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        raise "error: number of arguments provided is invalid"


    fileName = args[1]
    searchDate = args[2]

    try:
        dic = buildCounter(fileName)
        cookies = getMostActive(searchDate, dic)

        if not cookies:
            print("no result for given date")
        else:
            for cookie in cookies:
                print(cookie+"")
    except:
        raise "error: please check your arguments and try again"
