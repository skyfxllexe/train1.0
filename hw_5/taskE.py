n,k = map(int, input().split())
array, window = list(map(int, input().split())), dict()
minim, left, start, end, window_sum = 10e1000000000, 0,0,0,0,
for right, cur_number in enumerate(array):
    if cur_number not in window:
        window[cur_number] = 0
    window[cur_number] += 1
    window_sum += cur_number
    while len(window.keys()) == k:
        if len(window.keys()) == k:
            if window_sum < minim:
                minim, start, end = window_sum, left, right 
        window[array[left]] -= 1
        window_sum -= array[left]
        if window[array[left]] == 0: del window[array[left]]
        left += 1
        
print(start+1, end+1)