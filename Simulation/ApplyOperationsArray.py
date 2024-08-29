# Apply Operations on an Array

nums = [1, 2, 2, 1, 1, 0]
length = len(nums)

for x in range(length - 1):
    # print(x)
    if nums[x] == nums[x + 1]:
        # print("{} is a match".format(nums[x]))
        nums[x] *= 2
        nums[x + 1] = 0
        # print("Result is ",nums[x])
print(nums)
print("**************")
# Create a new list 'result' with the same size filled with zeros
result = [0] * length  # [0, 0, 0, 0, 0, 0]

result_index = 0
# Iterate through 'nums' to populate non-zero to new array 'result'
for num in nums:
    if num:
        result[result_index] = num
        result_index += 1
# Return New array 'result'
print(result)
