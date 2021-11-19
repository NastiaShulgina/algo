def valid(array, middle, aggressive_cows):
    cows_set = 1
    temp_element = array[0]
    for i in range(len(array)):
        if array[i] - temp_element >= middle:
            cows_set += 1
            temp_element = array[i]
            if cows_set >= aggressive_cows:
                return True
    return False


def main():
    aggressive_cows_amount = int(input("Amount of aggressive cows:"))
    stalls = list(map(int, input("Stalls:").split()))
    stalls.sort()
    right_stall = stalls[len(stalls) - 1]
    left_stall = 1
    distance = 0
    while left_stall < right_stall:
        middle_stall = left_stall + (right_stall - left_stall) // 2
        if valid(stalls, middle_stall, aggressive_cows_amount):
            distance = middle_stall
            left_stall = middle_stall + 1
        else:
            right_stall = middle_stall
    print("The min value of max distance: " + str(distance))


if __name__ == "__main__":
    main()
