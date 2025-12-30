# #  map fn

# def cube ( VARIABLE1):
#     return VARIABLE1*VARIABLE1*VARIABLE1

# l = [ 1,2,3,4,5]
# # cubel = []
# # for a in l :
# #     cubel.append(cube(a))

# cubel = list(map(cube , l))

# print(cubel)

# # CAN USE LAMBDA FN INSTEAD OF CUBE IN MAP , FILTER..
# #  FILTER

# def filter_fn(a) :
#     return a > 10
# newl = list(filter(filter_fn , cubel))
# print(newl)

from functools import reduce

no = [1,2,3,4,5,6]
sum = reduce (lambda x, y : x + y , no)

print(sum)
# output 15