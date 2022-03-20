"""
Given a list of integers of length >=4 return the average of first two and last two numbers """

n=input()
sum1=0
sum2=0
avg1=0
avg2=0
for i in range(0,2):
  sum1=sum1+int(n[i])
for i in range(len(n)-1,len(n)-3,-1):
    sum2=sum2+int(n[i])
avg1=sum1/2
avg2=sum2/2
print(avg1)
print(avg2)
