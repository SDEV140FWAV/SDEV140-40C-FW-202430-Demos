nums = [2,1,7,9]
nums1 = nums.copy()
myNum = 9
myNum = 7
print(nums[3])
nums[3] = 18
print(nums[3])
nums.append(19)
print(nums)
nums.insert(3,56)
print(nums)
nums.insert(56,4)
print(nums)
print(nums[6])
print(len(nums))
del nums[-1]
print(nums)

nums.pop()
print(nums)
nums.pop(3)
print(nums)
nums.append(9)
print(nums)

nums.remove(18)
print(nums)
#nums.remove(56)
#print(nums)
nums.sort()

#print(sorted(nums))
print(nums)
nums.reverse()
print(nums)
print(nums1)
nums1.reverse()
print(nums1)
nums1.reverse()
print(nums1)
print(len(nums))