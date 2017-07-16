def remove_adjacent(nums):
  a=[]
  for var1 in nums:
    b=nums.count(var1)
    if b==1:
      a.append(var1)
  # +++your code here+++
  print (a)
  return

remove_adjacent([1,2,2,3])
