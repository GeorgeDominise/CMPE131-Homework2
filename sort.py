def sort_list(input):
    input = []
    n = len(input)

    i = 0   

    while (i<n):
        j = i + 1
        while(j < n-i-1):
            if(input[i] > input[j]):
                temp = input[i]
                input[i] = input[j]
                input[j] = temp
            j = j + 1
        i = i + 1
    return(input)
