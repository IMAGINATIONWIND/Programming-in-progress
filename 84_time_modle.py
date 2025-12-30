import time
print("Number of seconds since 1st Jan 1970")
t= time.time()
print(t)
print(time.ctime())
print(time.localtime())
# now we can check the time taken to run a loop 

# for i in range(50000):
#     print(i)
# init=time.time()
# print(init-t)
# # same for while loop
# print('few moments later \n')
# time.sleep(5)
# i = 0
# t= time.time()
# while i < 50000:
#     print(i)
#     i = i+1
# init=time.time()
# print(init-t)