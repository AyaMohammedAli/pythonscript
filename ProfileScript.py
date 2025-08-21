
import time
import random

# A function that simulates slow computation
def slow_function():
    total = 0
    for i in range(100000):  # loop many times
        total += i * random.randint(1, 10)
    return total

# A function that simulates waiting (I/O)
def wait_function():
    time.sleep(2)  # simulating delay (like reading a file)
    return "Done waiting!"

# A function that combines them
def main():
    print("Starting profiling example...")
    result1 = slow_function()
    print("Result of slow_function:", result1)
    
    result2 = wait_function()
    print("Result of wait_function:", result2)

if __name__ == "__main__":
    main()
