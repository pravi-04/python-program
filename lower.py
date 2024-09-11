def lowerr(S):
    output_char=""
    for letter in S:
        if 'A' <= letter <= 'Z':
            output_char += chr(ord(letter)+32)
        else:
            output_char+=letter
    return output_char



S = "ABCddE"
output = lowerr(S)
print(output)