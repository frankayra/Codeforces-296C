import sys

def compute(k, array):
    if k == 1 or k == 0:
        return min(array)
    return max(array)

def main():
    input = sys.stdin.buffer.readline

    firstline = input().strip().split()
    secondline = input().strip().split()
    n = int(firstline[0])
    k = int(firstline[1])
    array = [int(item) for item in secondline]

    print(compute(k, array))
        

    

if __name__ == "__main__":
    main()