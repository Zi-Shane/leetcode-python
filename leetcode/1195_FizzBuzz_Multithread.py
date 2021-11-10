import threading
from typing import Callable


def printFizz() -> None:
    print("Fizz")
    
def printBuzz() -> None:
    print("Buzz")
    
def printFizzBuzz() -> None:
    print("FizzBuzz")
    
def printNumber(num: int) -> None:
    print(num)

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.semaphore_fizz = threading.Semaphore(0)
        self.semaphore_buzz = threading.Semaphore(0)
        self.semaphore_fizzbuzz = threading.Semaphore(0)
        self.semaphore_number = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        self.semaphore_fizz.acquire()
        printFizz()
        self.semaphore_number.release()


    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        self.semaphore_buzz.acquire()
        printBuzz()
        self.semaphore_number.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        self.semaphore_fizzbuzz.acquire()
        printFizzBuzz()
        self.semaphore_number.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        self.semaphore_number.acquire()
        for i in range(1, self.n+1):
            if i % 3 == 0:
                self.semaphore_fizz.release()
            elif i % 5 == 0:
                self.semaphore_buzz.release()
            elif i % 15 == 0:
                self.semaphore_fizzbuzz.release()
            else:
                self.semaphore_number.release()
                

    def run_jobs(self):
        self.zero_thread = threading.Thread(target=self.fizz, args=(printFizz,))
        # self.even_thread = threading.Thread(target=self.even, args=(printNumber,))
        # self.odd_thread = threading.Thread(target=self.odd, args=(printNumber,))
        self.zero_thread.start()
        # self.even_thread.start()
        # self.odd_thread.start()
        self.zero_thread.join()
        # self.even_thread.join()
        # self.odd_thread.join()

if __name__ == '__main__':
    sol = FizzBuzz(1)
    sol.run_jobs()
    print("Done.")
