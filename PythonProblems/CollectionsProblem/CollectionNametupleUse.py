from collections import namedtuple
N=int(input())

ColumnName=input().split()

Data=namedtuple('Marks', ColumnName )
studentDetails=[]
for i in range(N):
    a=input().split()
    student=Data(a[0],a[1],a[2],a[3])
    studentDetails.append(student)


totalMarks=0
for st in studentDetails:
    totalMarks+=int(st.MARKS)


print(totalMarks/N)
