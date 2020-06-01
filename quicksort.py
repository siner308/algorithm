def quicksort(x):
    if len(x) < 2:
        return x
    pivot = x[0]
    less = [i for i in x[1:] if compare(i, pivot)]
    greater = [i for i in x[1:] if not compare(i, pivot)]
    return quicksort(greater) + [pivot] + quicksort(less)
    
def compare(num1, num2):
    return num1 < num2
