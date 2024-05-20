# lambda function is uded with map[] and filter[]
nums = [8,2,1,3,5,6]
even = filter(lambda x:x%2 ==0, nums)
print(f"even = {even}")
even = list(even)
print(f"even = {even}")






