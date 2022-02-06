# 한 번 체크한 결과를 저장하는 비트 b (2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..) 
# 좌우 등 소리를 저장할 트랙 개수인 채널 c (모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.) 
# 녹음할 시간 s가 주어질 때, 필요한 저장 용량을 계산하는 프로그램을 작성해보자.

'''
입력
h, b, c, s 가 공백을 두고 입력된다.
h는 48,000이하, b는 32이하(단, 8의배수), c는 5이하, s는 6,000이하의 자연수이다.

44100 16 2 10

출력
필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
단, 소수점 둘째 자리에서 반올림해 첫째 자리까지 출력하고 MB를 공백을 두고 출력한다.

1.7 MB
'''

h, b, c, s = map(int, input().split())

result = h*b*c*s
resultMB = result / (8 * 1024**2)
print(round(resultMB, 1), 'MB')