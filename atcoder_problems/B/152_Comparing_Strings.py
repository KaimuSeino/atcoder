a, b = map(str, input().split())

str_list = []

def createStr(base_str, num):
    result = ''
    for _ in range(num):
        result += base_str
    
    return result

str_list.append(createStr(a, int(b)))
str_list.append(createStr(b, int(a)))
str_list.sort()

print(str_list[0])