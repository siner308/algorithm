#include <stdio.h>

#define INT_MAX 99999999

int makeitone(int, int);

int main(void){
    int inputnum = 0;
    int cntBase = 0;
    
    scanf("%d", &inputnum);
    printf("%d", makeOne(inputnum, cntBase));
    
    return 0;
}

int makeitone(int inputnum, int cntBase){
    int cnt[5];
    int minCnt = INT_MAX;
    int i = 0;
    
    for (i = 0; i < 5; i++){
    	cnt[i] = cntBase;
    }

    if(inputnum > 1){
	cnt[0] = ((inputnum % 3 == 0) ? (makeitone(inputnum/3, cnt[0] + 1)) : INT_MAX);
        cnt[1] = ((inputnum % 2 == 0) ? (makeitone(inputnum/2, cnt[1] + 1)) : INT_MAX);
        cnt[2] = (((inputnum - 1) % 3 == 0) ? (makeitone((inputnum - 1)/3, cnt[2] + 2)) : INT_MAX);
        cnt[3] = (((inputnum - 2) % 3 == 0) ? (makeitone((inputnum - 2)/3, cnt[3] + 3)) : INT_MAX);
        cnt[4] = (((inputnum - 1) % 2 == 0) ? (makeitone((inputnum - 1)/2, cnt[4] + 2)) : INT_MAX);
    }
	    
    if(cnt[0] < minCnt){
        minCnt = cnt[0];
    }
    if(cnt[1] < minCnt){
        minCnt = cnt[1];
    }
    if(cnt[2] < minCnt){
        minCnt = cnt[2];
    }
    if(cnt[3] < minCnt){
	minCnt = cnt[3];
    }
    if(cnt[4] < minCnt){
	minCnt = cnt[4];
    }
	
    return minCnt;
}
