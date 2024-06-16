from collections import deque

def max_kernel(num_list, k):
    if not num_list or k <= 0:
        return []

    result = []
    deq = deque()

    for i in range(len(num_list)):

        if deq and deq[0] < i - k + 1:
            deq.popleft()

        while deq and num_list[deq[-1]] <= num_list[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            result.append(num_list[deq[0]])

    return result

# Test the function
# num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
num_list = [4, 8, 9, 2, 24, 33, -100, 67, 8, 99, 65, 1]
k = 4
print(max_kernel(num_list, k))  # Output: [5, 5, 5, 5, 10, 12, 33, 33]
