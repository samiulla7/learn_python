'''
List Comprehension: Elegant way to create new List
List comprehension consists of an expression followed by for statement inside square brackets.
'''
pow2 = [2 ** x for x in range(10)]
print(pow2)
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# This code is equivalent to
# pow2 = []
# for x in range(10):
#    pow2.append(2 ** x)

#####################################################################################3

print([x for x in range(20) if x % 2 == 1])
# Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

[x+y for x in ['Python ','C '] for y in ['Language','Programming']]
# Output: ['Python Language', 'Python Programming', 'C Language', 'C Programming']

