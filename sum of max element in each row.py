def maximum(input):
    lst=[]
    max_sum = 0
    n=len(input)
    for row in input:
        max_row_element=float('-inf')
        for element in row:
                if element > max_row_element:
                    max_row_element=element
        lst.append(max_row_element)
        max_sum+=max_row_element

    return max_sum
input = [[3,2,4],[1,7,8],[5,9,6]]

output = maximum(input)
print(output)