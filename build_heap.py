def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        min_index = i
        left_child = 2 *i +1
        right_child = left_child +1
        if left_child < n and data[left_child] <data[min_index]:
            min_index=left_child
        if right_child<n and data[right_child] < data[min_index]:
            min_index = right_child
        if i != min_index:
            swaps.append((i,min_index))
            data[i], data[min_index] = data[min_index], data[i]
            while min_index* 2+1 <n:
                j=min_index*2+1
                if j< n-1 and data[j+1] < data[j]:
                    j+=1
                if data[min_index]> data[j]:
                    swaps.append((min_index,j))
                    data[min_index],data[j] = data[j], data[min_index]
                    min_index =j
                else:
                    break
    return swaps


def main():
    try:
        text = input("Enter I or F: ")
        if text not in ["I", "F"]:
            raise ValueError("Invalid input, expected 'I' or 'F'")
        if text == "I":
            n = int(input())
            data = list(map(int, input().split()))
            if len(data) != n:
                raise ValueError(f"Invalid input, expected {n} elements")
            swaps = build_heap(data)
            print(len(swaps))
            for i, j in swaps:
                print(i, j)
        elif text == "F":
            filename = input()
            file_path = f"./text/{filename}"
            if "a" not in filename:
                try:
                    with open(file_path) as f:
                        n = int(f.readline())
                        data = list(map(int, f.readline().split()))
                        if len(data) != n:
                            raise ValueError(f"Invalid input, expected {n} elements")
                        swaps = build_heap(data)
                        print(len(swaps))
                        for i, j in swaps:
                            print(i, j)
                except FileNotFoundError:
                    print(f"Error: File {filename} not found")
                except:
                    print("Error: Invalid input in file")
    except ValueError as e:
        print(f"Error: {str(e)}")
