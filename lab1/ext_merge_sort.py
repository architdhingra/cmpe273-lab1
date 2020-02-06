import os
import time

allLines = []
def writeToFile(sortedAr):
    global x
    x = 1
    f = open("C:/Users/Archit/Documents/Projects/273/cmpe273-spring20-labs/lab1/output/sorted_"+str(x)+".txt","w+")
    x = x+1
    for item in sortedAr:
        f.write(str(item)+"\n")
    f.close()

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

def readFiles(file):
    time.sleep(1)
    for line in file:
        allLines.append(int(line.strip('\n')))
    time.sleep(1)
    
def openFiles():
    fileList = os.listdir(path)
    file = []
    for i in fileList:
        y = open(os.path.join(path+i), 'r')
        file.append(y)
    return file 
    
if __name__ == "__main__":    
    start_time = time.time()
    print (start_time)
    div = []
    file = openFiles()
    for q in range(len(file)):
        readFiles(file[q])
    sortedArr = mergeSort(allLines)
    writeToFile(sortedArr)
    print("--- {} seconds ---{}".format((time.time() - start_time),time.time()))