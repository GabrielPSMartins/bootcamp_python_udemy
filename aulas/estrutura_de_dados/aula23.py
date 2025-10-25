# List comprehension com strings

frutas1 = ['maçã', 'banana', 'laranja', 'uva']

# for i in frutas1:
#     if 'b' in i:
#         frutas2.append(i)

frutas2 = [i for i in frutas1 if 'b' in i]    

print(frutas2)