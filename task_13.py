import time
from functools import wraps

def cached(max_size=None, seconds=None):
    # проверка корректности max_size
    if not isinstance(max_size, int) or max_size <= 0:
        max_size = None

    # проверка корректности seconds
    if not isinstance(seconds, int) or seconds <= 0:
        seconds = None

    def decorator(func):
        cache = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # формируем ключ из args и kwargs
                key = (args, tuple(sorted(kwargs.items())))
            except Exception:
                # если аргументы не хешируемые
                return func(*args, **kwargs)
            
            current_time = time.time()

            # удаляем устаревшие записи
            if seconds is not None:
                expired_keys = []

                for k, (result, saved_time) in cache.items():
                    if current_time - saved_time > seconds:
                        expired_keys.append(k)

                for k in expired_keys:
                    cache.pop(k, None)

            # если значение есть в кэше
            if key in cache:
                result, saved_time = cache[key]

                # проверяем срок жизни
                if seconds is None or current_time - saved_time <= seconds:
                    return result
                
            # вычисляем результат
            try:
                result = func(*args, **kwargs)
            except Exception:
                # код не должен ломатся
                return None
            
            # ограничение размера кэша
            if max_size is not None and len(cache) >= max_size:
                oldest_key = next(iter(cache))
                cache.pop(oldest_key, None)

            # сохраняем в кэш
            cache[key] = (result, current_time)

            return result
        
        return wrapper
    
    return decorator

@cached(max_size=3, seconds=10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2

# Первый вызов — вычисляется
print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4

# Повторный вызов с теми же аргументами — берётся из кэша
print(slow_function(2)) # Вывод: 4 (без вычисления)

# Через 15 секунд кэш устареет, и будет новое вычисление
time.sleep(15)
print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4


# @cached(max_size=2, seconds=5)
# def add(a, b):
#     print("Вычисление...")
#     return a + b


# print(add(1, 2))  # Вычисление...
# print(add(1, 2))  # Берётся из кэша

# time.sleep(6)

# print(add(1, 2))  # Кэш устарел → снова вычисление