# =============================
# 1. Imports
# =============================
import time
import matplotlib.pyplot as plt

# =============================
# 2. Sorting Algorithms
# =============================

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = merge_sort(arr[:mid])
        R = merge_sort(arr[mid:])
        return merge(L, R)
    return arr

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# =============================
# 3. Input Arrays
# =============================

Arr1 = list(range(1, 6))
Arr2 = list(range(1, 11))
Arr3 = list(range(1, 51))
Arr4 = list(range(1, 101))
inputs = [Arr1, Arr2, Arr3, Arr4]
sizes = [len(arr) for arr in inputs]

# =============================
# 4. Timing Function
# =============================

def average_time(sort_func, data, repeats=5):
    total_time = 0
    for _ in range(repeats):
        start = time.perf_counter()
        sort_func(data)
        end = time.perf_counter()
        total_time += (end - start)
    return (total_time / repeats) * 1000  # Convert to milliseconds

# =============================
# 5. Main Logic
# =============================

sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort
}

results = {name: [] for name in sorting_algorithms}

for name, func in sorting_algorithms.items():
    for arr in inputs:
        avg_time = average_time(func, arr)
        results[name].append(avg_time)

# =============================
# 6. Plotting
# =============================

for name, times in results.items():
    plt.plot(sizes, times, marker='o', label=name)

plt.title("Empirical Time Complexity of Sorting Algorithms")
plt.xlabel("Input Size (N)")
plt.ylabel("Average Execution Time (ms)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
