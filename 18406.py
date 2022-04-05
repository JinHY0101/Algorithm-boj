point = input()
num_of_left = 0
num_of_right = 0
 
for i in range(len(point)//2):
  num = int(point[i])
  num_of_left += num
 
for i in range(len(point)//2, len(point)):
  num = int(point[i]) 
  num_of_right += num
 
if num_of_left == num_of_right:
  print("LUCKY")
else:
  print("READY") 