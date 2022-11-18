# #это смотреть не надо!!!!
# #это я для себя смотрела, разбиралась как оно работает
# def benchmark(func):
#     import time
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end-start))
#         return return_value
#     return wrapper
#
#
# @benchmark
# def fetch_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage.text
#
# webpage = fetch_webpage('https://tproger.ru/translations/demystifying-decorators-in-python/')
# print(webpage)
#
#
# from collections import deque
#
# class Memoized:
#     def __init__(self, cache_size=100):
#         self.cache_size = cache_size
#         self.call_args_queue = deque()
#         self.call_args_to_result = {}
#
#     def __call__(self, fn):
#         def new_func(*args, **kwargs):
#             memoization_key = self._convert_call_arguments_to_hash(args, kwargs)
#             if memoization_key not in self.call_args_to_result:
#                 result = fn(*args, **kwargs)
#                 self._update_cache_key_with_value(memoization_key, result)
#                 self._evict_cache_if_necessary()
#             return self.call_args_to_result[memoization_key]
#         return new_func
#
#     def _update_cache_key_with_value(self, key, value):
#         self.call_args_to_result[key] = value
#         self.call_args_queue.append(key)
#
#     def _evict_cache_if_necessary(self):
#         if len(self.call_args_queue) > self.cache_size:
#             oldest_key = self.call_args_queue.popleft()
#             del self.call_args_to_result[oldest_key]
#
#     @staticmethod
#     def _convert_call_arguments_to_hash(args, kwargs):
#         return hash(str(args) + str(kwargs))
#
#
# @Memoized(cache_size=5)
# def get_not_so_random_number_with_max(max_value):
#     import random
#     return random.random() * max_value