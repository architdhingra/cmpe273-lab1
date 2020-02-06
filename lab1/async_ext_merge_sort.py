import os
import asyncio
import time

x = 1
allLines = []
def writeToFile(sortedAr):
    global x
    f = open("C:/Users/Archit/Documents/Projects/273/cmpe273-spring20-labs/lab1/output/sorted_"+str(x)+".txt","w+")
    x = x+1
    for item in sortedAr:
        f.write(str(item)+"\n")
    f.close()
    return 0

def mergeSort(list):
    length = len(list)
    if length < 2:
        return list
    med = length//2
    left = list[:med]
    right = list[med:]
    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    final = []

    while left and right:
        i = left[0]
        j = right[0]

        if i < j:
            final.append(i)
            left.pop(0)
        else:
            final.append(j)
            right.pop(0)

    while left:
        final.append(left[0])
        left.pop(0)

    while right:
        final.append(right[0])
        right.pop(0)

    return final

path = "C:/Users/Archit/Documents/Projects/273/cmpe273-spring20-labs/lab1/input/"

async def readLine(file):
    #print("reading 1 :",file.name)
    await asyncio.sleep(1)
    for line in file:
        allLines.append(int(line.strip('\n')))
    await asyncio.sleep(1)
    #print("reading 2 :",file.name)
    return allLines

def openFiles():
    fileList = os.listdir(path)
    file = []
    for i in fileList:
        y = open(os.path.join(path+i), 'r')
        file.append(y)
    return file 


async def main():
    div = []
    file = openFiles()
    for q in range(len(file)):
        div.append((readLine(file[q])))
    allLines = await asyncio.gather(div[0],div[1],div[2],div[3],div[4],div[5],div[6],div[7],div[8],div[9])
    sortedArr = mergeSort(allLines[0])
    writeToFile(sortedArr)

if __name__ == "__main__":
    start_time = time.time()
    print (start_time)
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    finally:
        loop.close()
    print("--- {} seconds ---{}".format((time.time() - start_time),time.time()))