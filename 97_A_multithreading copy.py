import threading
import time

def fn1(input1):
    print(f"This work will take {input1} seconds for Person A to complete")
    time.sleep(input1)
    print("Person A completed")
    
def fn2(input2):
    print(f"This work will take {input2} seconds for Person B to complete")
    time.sleep(input2)
    print("Person B completed")
    
def fn3(input3):
    print(f"This work will take {input3} seconds for Person C to complete")
    time.sleep(input3)
    print("Person C completed")

time1 = time.perf_counter()

#Begineer code 

fn1(3)
fn2(5)
fn3(7)

time2 = time.perf_counter()

print(time2-time1)

#Same using Threading

t1 = threading.Thread(target=fn1 , args=[3])
t2 = threading.Thread(target=fn2 , args=[5])
t3 = threading.Thread(target=fn3 , args=[7])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time3 = time.perf_counter()

print(time3-time2)