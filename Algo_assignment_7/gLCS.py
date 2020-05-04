def dataLoad(path):
    file = open(path)
    return file.readline().strip(),file.readline().strip()

def lcs(a,b):
    a_len = len(a)
    b_len = len(b)
    dp = []
    for i in range(a_len + 1):
        dp.append([0 for j in range(b_len + 1)])
    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            elif j-2 >0 and j < b_len and a[i-1] != b[j-1] and a[i-1] != b[j-2] and a[i-1] != b[j]:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j - 1]) if dp[i-1][j] != 0 or dp[i][j-1] !=0 else 0  
    max_length = max(max(dp))
    return dp, max_length

def get_path(a, b, dp, i, j):
    if i == 0 or j == 0:
        return ""
    if a[i-1] == b[j-1]:
        return get_path(a, b, dp, i-1, j-1) + a[i-1]
    else:
        if dp[i-1][j] > dp[i][j-1]:
            return get_path(a, b, dp, i-1, j)
        elif dp[i-1][j] == 0 and dp[i][j-1] == 0 and dp[i-1][j-1] == 0:
            return ""
        else:
            return get_path(a, b, dp, i, j-1)
        
def Maxindex(dp):
    Max = 0
    H = 0
    j = 0 
    for i in range(len(dp)):
        Max=max(Max,max(dp[i]))
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if (dp[i][j] == Max):
                H,T = i,j
    return H,T
            
A,B = dataLoad('./gLCS.inp')
dp, leng = lcs(A,B)
file = open('./gLCS.out','w')
i,j = Maxindex(dp)
string = get_path(A,B,dp,i,j)
file.write(string)