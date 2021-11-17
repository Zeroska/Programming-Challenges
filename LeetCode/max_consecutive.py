def findMaxConsecutiveOnes(nums):
    max_consecutive = 0
    count = 0
    for i in range(len(nums)):
        max_consecutive = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            if count > max_consecutive: 
                max_consecutive = count
            if nums[i] == 0:
                count = 0
    return max_consecutive



def main():
    test = [1,1,0,1,1,1]
    print(findMaxConsecutiveOnes(test))


if __name__ == '__main__':
    main()