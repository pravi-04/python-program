
def maximum(input):
    lst={}
    n=len(input)
    for i in input:
        lst[i]=len(i)

    maxi=float('-inf')
    maximum={}
    for j in lst:
        if lst[j]>maxi:
            maxi=lst[j]
            maximum[j]=lst[j]
    return list(maximum.items())[-1]


input=['fan','bottle','flower','alphabet','watch','watermelon']
output=maximum(input)
print(output)