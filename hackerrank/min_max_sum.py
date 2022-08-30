def miniMaxSum(arr):
    sorted_array = sorted(arr)
    minValues = sorted_array[:4]
    maxValues = sorted_array[-4:]
    
    print(f'{sum(minValues)} {sum(maxValues)}')
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
