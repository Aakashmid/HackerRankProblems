'''
>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
'''
# print(list(zip([1,2,3,4,5,6],'Hacker')))
# print(list(zip([1,2,3],[2,3,5],[3,8,9])))

N,S=input().split()
N,S=int(N),int(S)

marks=[] # marks of all studensts 
for i in range(S):
    marks.append(list(map(float,input().split())))

marks_each_subject=list(zip(*marks))
for stu in marks_each_subject:
    print(sum(stu)/len(stu))