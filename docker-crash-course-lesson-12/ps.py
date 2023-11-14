t = int(input())

for _ in range(t):
    n, m, k, H = map(int, input().split())
    h = list(map(int, input().split()))
    
    count = 0
    for person_height in h:
        for step in range(1, m + 1):
            height_difference = abs(H - person_height) - step * k
            print("###")
            print(height_difference)
            print("###")

            if height_difference == 0:
                count += 1
                break
                
    print(count)
