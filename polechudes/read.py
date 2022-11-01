def log (filename ="log.py"):
    file =open(filename,"r")
    record = int (file.read())
    iterations = int(file.read)
    words=[]
    for i in range(0,iterations):
        words.append(file.readline())
    result = [record, iterations, words]
    return result;


def record