def largestElement():
        nums = []
        length = int(input("enter len:"))

        while len(nums) < length:
            value = int(input("enter values:"))
            nums.append(value)
        largest = nums[0]
        for i in nums:
             if i > largest:
                  largest = i
        print("largest num is:",largest)
largestElement()