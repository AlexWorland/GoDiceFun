from matplotlib import pyplot as plt
import os

def main():
    files = openFiles()
    data = []
    for file in files:
        for line in file:
            data.append(int(line))
    counts = analyzeData(data)
    plotData(counts)

def readFile(file):
    # read the data from the file
    # return a list of the data
    data = []
    for line in file:
        data.append(int(line))
    return data

def analyzeData(data):
    # count instance of each number in data
    # return a list of the counts
    print(data)
    counts = []
    for i in range(1, 20):
        counts.append(data.count(i))
    return counts

def plotData(data):
    # plot data as a bar graph
    print(data)
    plt.bar(range(1, 20), data)
    # set the x axis to be the numbers 1-20
    plt.xticks(range(1, 20))
    plt.show()

def openFiles():
    # open all files that start 'dice_rolls_' and end with '.csv'
    # return a list of the files
    files = []
    for file in os.listdir():
        if file.startswith("dice_rolls_") and file.endswith(".csv"):
            files.append(open(file, 'r'))
    return files

        

if __name__ == "__main__":
    main()
    