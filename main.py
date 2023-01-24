array = [3,3,5,4,10,11,12]
n = len(array)
for i in range(0,n):
   for j in range(i+1,n):
      if(array[i]>array[j]):
        temp=array[i]
        array[i]=array[j]
        array[j]=temp
  print(array)
