import os
import time

from threading import Thread, current_thread
from multiprocessing import Process, current_process
from time import sleep


sleep(2)
def read_file(w:list):
    p_id = os.getpid()
    print(f"{p_id}-----{current_process().name}----------{current_thread().name}----kutish boshlandi")
    s = 1
    f = 1
    for char in w:
        num = int(char)
        if num % 2 == 0:
            s *= num
        elif num % 2 == 1:
            f *= num
    print(f"natija  {abs(s-f)}")
    print(f"{p_id}-----{current_process().name}----------{current_thread().name}----kutish tugadi")



if __name__=="__main__":
    s_time=time.time()
    ter=[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]
    read_file(ter)
    e_time=time.time()
    print(s_time-e_time)
    print()
    t = Thread(target=read_file, args=(ter,))
    t3 = Thread(target=read_file, args=(ter,))
    t.start()
    t3.start()
    t.join()
    t3.join()
    e_time = time.time()
    print(s_time - e_time)
    print()

    p1 = Process(target=read_file, args=(ter,))
    p2 = Process(target=read_file, args=(ter,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    e_time = time.time()
    print(s_time - e_time)


