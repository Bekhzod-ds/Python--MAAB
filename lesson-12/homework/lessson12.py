import threading

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    for num in range(start, end):
        if is_prime(num):
            result.append(num)

def threaded_prime_checker(start, end, num_threads):
    threads = []
    results = [[] for _ in range(num_threads)]
    step = (end - start) // num_threads

    for i in range(num_threads):
        sub_start = start + i * step
        sub_end = start + (i + 1) * step if i < num_threads - 1 else end
        thread = threading.Thread(target=check_primes, args=(sub_start, sub_end, results[i]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Flatten the list of results
    all_primes = [prime for sublist in results for prime in sublist]
    all_primes.sort()
    print(f"Prime numbers from {start} to {end}:")
    print(all_primes)
  
# example usage:
threaded_prime_checker(1, 100, 4)

import threading
from collections import Counter
import os

def process_lines(lines, result_list):
    counter = Counter()
    for line in lines:
        words = line.strip().lower().split()
        counter.update(words)
    result_list.append(counter)

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    step = total_lines // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i < num_threads - 1 else total_lines
        result_list = []
        thread = threading.Thread(target=process_lines, args=(lines[start:end], result_list))
        threads.append((thread, result_list))
        thread.start()

    final_counter = Counter()

    for thread, result_list in threads:
        thread.join()
        final_counter.update(result_list[0])

    print("Word frequency summary:")
    for word, count in final_counter.most_common(10):
        print(f"{word}: {count}")

# Example usage
file_path = "sample.txt"
if os.path.exists(file_path):
    threaded_word_count(file_path)
else:
    print("File not found. Please place a sample.txt file in the same directory.")
