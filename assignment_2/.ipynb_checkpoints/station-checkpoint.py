import math

inp = open('./station.inp',"r")
out = open('./station.out',"w")
A = [float(i) for i in inp.readline().split()]
B = [float(i) for i in inp.readline().split()]
P = [float(i) for i in inp.readline().split()]
u1 = [B[0] - A[0], B[1] - A[1], B[2]-A[2]] # 직선의 방향 벡터 
distance = []

isright = False
t = 1
while not isright:
    S = [t*B[0] + (1-t)*A[0], t*B[1] + (1-t)*A[1], t*B[2] + (1-t)*A[2]]
    u2 =[S[0] - P[0], S[1] - P[1], S[2] - P[2]] # S위 임의의 점 T와 P의 방향벡터 
    if u1 == [0,0,0]:
        angleValue = (u1[0]*u2[0] + u1[1]*u2[1] + u1[2]*u2[2])/ math.sqrt(u2[0]**2 + u2[1]**2 + u2[2]**2)
    elif u2 == [0,0,0]:
        angleValue = (u1[0]*u2[0] + u1[1]*u2[1] + u1[2]*u2[2])/(math.sqrt(u1[0]**2 + u1[1]**2 + u1[2]**2))
    else :
        angleValue = (u1[0]*u2[0] + u1[1]*u2[1] + u1[2]*u2[2])/((u1[0]**2 + u1[1]**2 + u1[2]**2)*(u2[0]**2 + u2[1]**2 + u2[2]**2))**0.5
    if angleValue > 1 :
        angleValue = 1
    angle = math.degrees(math.acos(angleValue))
    # t 는 더하면 B쪽으로 
    # t 는 뺴면 A쪽으로
    # 0 < t < 1
    t -=0.0001
    t = round(t,4)
    Distance = ((S[0] - P[0])**2 + (S[1] - P[1])**2 + (S[2] - P[2])**2)**0.5
    distance.append(Distance)
    if t == 0:
        print("t == 0")
        isright = True
Distance = int(min(distance)//1 + 1)

      
out.write(str(Distance)+'\n')
out.close()
inp.close()