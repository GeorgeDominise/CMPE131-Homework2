def sort_list(input):
    n = len(input)
    i = 1   
    while (i<n):
        j = 0
        while(j <= n-i-1):
            if(input[j+1] < input[j]):
                input[j+1], input[j] = input[j], input[j+1]
            j = j + 1
        i = i + 1
    return input

input = [21, 54, 63, 11, 31, 44]
sort_list(input)
print(input)
