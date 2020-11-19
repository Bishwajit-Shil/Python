
def average_finder(*args):
    average= []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return  average  

average = average_finder([1,2,4],[1,4,5])
print(average)