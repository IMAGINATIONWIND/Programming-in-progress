import threading
import time
from concurrent.futures import ThreadPoolExecutor
'''concurrent is more easier and practical
'''
def fn1(input1):
    print(f"This work will take {input1} seconds for Person A to complete")
    time.sleep(input1)
    print("Person A completed")
    return input1
# def fn2(input2):
#     print(f"This work will take {input2} seconds for Person B to complete")
#     time.sleep(input2)
#     print("Person B completed")
    
# def fn3(input3):
#     print(f"This work will take {input3} seconds for Person C to complete")
#     time.sleep(input3)
#     print("Person C completed")

def main():
    time1 = time.perf_counter()

    #Begineer code 

    # fn1(3)
    # fn2(5)
    # fn3(7)

    time2 = time.perf_counter()

    # print(time2-time1)

    #Same using Threading

    t1 = threading.Thread(target=fn1 , args=[3])
    t2 = threading.Thread(target=fn1 , args=[5])
    t3 = threading.Thread(target=fn1 , args=[7])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    time3 = time.perf_counter()

    print(time3-time2)
    

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future = executor.submit(fn1,3)
        # future = executor.submit(fn1,5)
        # future = executor.submit(fn1,6)
        # print(future.result())
        # print(future.result())
        # print(future.result())

        t =[ 1,2,3,4,5]
        results = executor.map(fn1,t)
        for result in results:
            print(result)
    
    
poolingDemo()