#선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]

print(array)

#삽입 정렬
#데이터가 거의 정렬되어 있을 때 훨씬 효율적이다.(거의 데이터가 정렬되어 있다면 삽입 정렬) 선택 정렬은 아님
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]: #한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)

#퀵 정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

#파이썬 라이브러리
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
array.sort(reverse=True)
print(array)
