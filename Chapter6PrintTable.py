#automate the boring stuff with python (page142-143)
#chapter 6
tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(data):
    colWidths = [0] * len(tableData) #create a list containing the same number of 0 values
    # and the number of inner lists in tableData
    for i in colWidths:
        colWidths = max(data[i]) #store maximum width of each column as a list of integer

    y = len(colWidths)

    for x in range(len(data[0])):
        print(str(data[0][x]).rjust(y) + str(data[1][x]).rjust(y) + str(data[2][x]).rjust(y))


printTable(tableData)

