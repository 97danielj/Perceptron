import numpy as np
from numpy.linalg import inv

a= np.array([2, 1])
print(a) #벡터 선(1차원 배열)
print(np.linalg.norm(a))
행렬1 = np.array([[1,2],[3,4]]) #행렬 면
print(행렬1)
m1 = np.array([[1,2],[3,4]])
m2 = np.array([[1,2],[3,4]])
print(m1*m2)
print(m1+m2)
i_m1=inv(m1)
#행렬 내적
print(np.dot(m1,m2))
x=np.array([1,2,3])
y=np.array([4,5,6])
#벡터 내적
print(np.dot(x,y))

m_x=np.array([[1,2,3]])
m_y=np.array([[4,5,6]])
print(m_x)
print(m_y)
print(m_x.shape)
print(m_y.shape)
m_y=m_y.T
print(m_y)
print(m_y.shape)
print(np.dot(m_x,m_y))


