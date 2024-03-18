import time

def measure_speed(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання функції {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper

@measure_speed
def tuple():
    tuple_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(tuple_data)
    return tuple_data


@measure_speed
def list():
    list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list_data)
    return list_data


tuple()
list()
