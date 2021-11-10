import threading

class ZeroEvenOdd():
    def __init__(self, n, printNumber): # constructor
        self.n = n
        self.semaphore_zero = threading.Semaphore(1)
        self.semaphore_even = threading.Semaphore(0)
        self.semaphore_odd = threading.Semaphore(0)

    def zero(self, printNumber): # only output 0's
        for i in range(1, self.n+1):
            self.semaphore_zero.acquire()
            printNumber(0)
            if i % 2 != 0:
                self.semaphore_odd.release()  # 讓odd可以跑
            else:
                self.semaphore_even.release()  # 讓even可以跑

    def even(self, printNumber): # only output even numbers
        for i in range(2, self.n+1, 2):
            self.semaphore_even.acquire()
            printNumber(i)
            self.semaphore_zero.release()  # 讓zero可以跑

    def odd(self, printNumber): # only output odd numbers
        for i in range(1, self.n+1, 2):
            self.semaphore_odd.acquire()
            printNumber(i)
            self.semaphore_zero.release()  # 讓zero可以跑
            
    
    def run_jobs(self):
        self.zero_thread = threading.Thread(target=self.zero, args=(printNumber,))
        self.even_thread = threading.Thread(target=self.even, args=(printNumber,))
        self.odd_thread = threading.Thread(target=self.odd, args=(printNumber,))
        self.zero_thread.start()
        self.even_thread.start()
        self.odd_thread.start()
        self.zero_thread.join()
        self.even_thread.join()
        self.odd_thread.join()

def printNumber(n):
    print(n, end="")

obj = ZeroEvenOdd(5, printNumber)
obj.run_jobs()


# semaphore = threading.Semaphore(2)
# first_thread = threading.Thread(target = thread_first_job)
# second_thread = threading.Thread(target = thread_second_job)
# first_thread.start()
# second_thread.start()
# first_thread.join()
# second_thread.join()
