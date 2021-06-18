data = [[2,0], [4,0], [6,0], [8,1], [10,1], [12,1],[14,1]]

x_data = [i[0] for i in data] #공부한 시간 데이터
y_data = [i[1] for i in data] #합격 여부

import matplotlib.pyplot as plt

plt.scatter(x_data, y_data)
plt.xlim(0,15)
plt.ylim(-.1,1.1)

#기울기 a와 절편 b의 값 초기화
a=0
b=0

#학습률
lr = 0.05  

#시그모이드 함수 정의
def sigmoid(x):
    return 1 / (1+ np.e ** (-x))


#경사하강법 실행
#1,000번 반복될 때마다 각 x_data값에 대한 현재의 a값, b값 출력
for i in range(2001):
    for x_data, y_data in data:
        a_diff = x_data*(sigmoid(a*x_data+b)-y_data)
        b_diff = sigmoid(a*x_data+b)-y_data
        a = a -lr*a_diff
        b = b - lr* b a_diff
        if i % 1000 ==0:
            print("epoch=%.f, 기울기=%.04f, 절펴=%.04f" %(i,a,b))
        plt.scatter(x,y)
        plt.xlim(0,15)
        plt.ylim(-.1,1.1)
        x_range = (np.arange(0,15,0.1))
        plot.plot(np.arange(0,15,0.1), np.array([sigmoid(a*x +b)for x in x_range]))
        plt.show()




