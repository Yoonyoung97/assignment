def dataLoad(Path):
    if Path == "":
        file = open("./tube.inp")
    else:
        file = open(Path)
    Total = int(file.readline().strip())
    file.readline().strip();
    category = [int(i) for i in file.readline().strip().split()]
    category.sort(reverse=True)
    file.close()
    return Total, category

def remainMax(Total, Category):
    remainderMax = 10000000;
    for i in range(len(Category)):
        remainderMax = min(Total%Category[i],remainderMax)
    return remainderMax
#첫번째: 접근 나머지를 이용해보자
def find_element(Total, Category):
    remainderMax = remainMax(Total,Category)
    for i in Category:
        if Total%i == remainderMax:
            return i
def solution_using_remainder(T,C):
    """
    테스트케이스 10번 빼고 다 정답 90점
    """
    count = 0 
    element = find_element(T,C) 
    while T- element >= 0:
        element = Greedy_ver1(T,C)
        count+=1
        T = T - element
    if T != 0:
        count = 0
    else:
        count = count
    return count




def DataWrite(count):
    file = open("./tube.out" ,"w")
    file.write(str(count))
    file.close()

if __name__ =="__main__":    
    T , C = dataLoad("")
    count = solution_using_remainder(T,C)
    DataWrite(count)
