def sort_list(input):
    input = []
    n = len(input)
    for i in range(1, Number + 1):
        value = int(input("Please enter the value of Elements : " %i))
        input.append(value)
    
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
    print(input)

