## Multiprocessing with process pool executor
from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"Square: {number*number}"

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
if __name__=="__main__":
    t=time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_number,numbers)
    
    for result in results:
        print(result)
    
    finished_time=time.time()-t
    print(finished_time)