def makeOne(inputnum, cntBase):
    cnt = [cntBase, cntBase, cntBase, cntBase, cntBase]
    minCnt = INT_MAX
    if(inputnum > 1):
        cnt[0] = ((inputnum % 3 == 0) and (makeOne(inputnum/3, cnt[0] + 1)) or INT_MAX)
        cnt[1] = ((inputnum % 2 == 0) and (makeOne(inputnum/2, cnt[1] + 1)) or INT_MAX)
        cnt[2] = (((inputnum - 1) % 3 == 0) and (makeOne((inputnum - 1)/3, cnt[2] + 2)) or INT_MAX)
        cnt[3] = (((inputnum - 2) % 3 == 0) and (makeOne((inputnum - 2)/3, cnt[3] + 3)) or INT_MAX)
        cnt[4] = (((inputnum - 1) % 2 == 0) and (makeOne((inputnum - 1)/2, cnt[4] + 2)) or INT_MAX)
    
    if(cnt[0] < minCnt):
        minCnt = cnt[0]
    if(cnt[1] < minCnt):
        minCnt = cnt[1]
    if(cnt[2] < minCnt):
        minCnt = cnt[2]
    if(cnt[3] < minCnt):
        minCnt = cnt[3]
    if(cnt[4] < minCnt):
        minCnt = cnt[4]    
    return minCnt

cntBase = 0
inputnum = input()   
INT_MAX = 99999999
print(makeOne(inputnum, cntBase))
