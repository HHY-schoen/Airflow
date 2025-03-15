import logging

# 設定 logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# 主程式區塊
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print("結果:", sorted_arr)
    logger.info("泡泡序列測試OK!")
