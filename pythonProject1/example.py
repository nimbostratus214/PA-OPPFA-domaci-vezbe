import random
import time

# generate random list
def random_list (min, max, num_of_elements) -> object:
    list = random.sample(range(min, max), num_of_elements)
    # generate list of num_of_elements elements
    # element value is in range [min, max)
    return list

def foo(l):
    print("list: ", l)


l = random_list(1, 100, 50)

# meassure time:
start_time = time.perf_counter()
# float value in seconds: time.perf_counter()
# integer value in nanoseconds: time.perf_counter_ns()

foo(l)

end_time = time.perf_counter() - start_time

print("Duration: ", end_time)
