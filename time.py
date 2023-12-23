import time

def measure_time_complexity(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def example_function(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += i * j
    return result

n = 1000
elapsed_time = measure_time_complexity(example_function, n)
print(f"Elapsed time for n={n}: {elapsed_time} seconds")
