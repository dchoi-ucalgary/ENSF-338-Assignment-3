def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2

    return li

def processdata2(li):
    j = 2**len(li)

    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= j
    return li

print(processdata([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(processdata2([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

