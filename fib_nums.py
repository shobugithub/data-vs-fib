class Fibonacci:
    def __init__(self, stop):
        self.prev = 0
        self.current = 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            result = self.current
            self.prev, self.current = self.current, self.prev + self.current
            return result


stop_num = int(input("Enter a number: "))
fib_list = Fibonacci(stop_num)
for i in fib_list:
    print(i)

"""class FibonacciIterator:
    def __init__(self, stop_num):
        self.stop_num = stop_num
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.stop_num:
            raise StopIteration
        else:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result

# Example usage:
stop_num = 100  # Fibonacci numbers will be generated until this number is reached
fibonacci_iter = FibonacciIterator(stop_num)
for num in fibonacci_iter:
    print(num)
"""