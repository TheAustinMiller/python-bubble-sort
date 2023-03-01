def swap_them(a, b, nums):
  temp = nums[a]
  nums[a] = nums[b]
  nums[b] = temp
  return nums

list = [5, 3, 10, 9, 2, 1, 15, 8]

have_swapped = True
while have_swapped:
  have_swapped = False
  for i in range(len(list) - 1):
    if list[i] > list[i+1]:
      list = swap_them(i, i+1, list)
      have_swapped = True
print(list)
