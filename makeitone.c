#include <stdio.h>

#define INT_MAX 99999999

int makeOne(int, int);

int main(void){
    int input = 0;
    int cnt = 0;
    
    scanf("%d", &input);
    printf("%d", makeOne(input, cnt));
    
    return 0;
}

int makeOne(int input, int cntBase){
    int cnt[5];
    int minCnt = INT_MAX;
    int i = 0;
    
    for (i = 0; i < 5; i++){
    	cnt[i] = cntBase;
	}

	    if(input > 1){
	        if(input % 3 == 0){
	            cnt[0] = makeOne(input/3, cnt[0] + 1);
	        }
	        else{
	        	cnt[0] = INT_MAX;
			}
	
	        if(input % 2 == 0){
	            cnt[1] = makeOne(input/2, cnt[1] + 1);
	        }      
	        else{
	        	cnt[1] = INT_MAX;
			}
	        
	        if((input - 1) % 3 == 0){
	            cnt[2] = makeOne((input - 1)/3, cnt[2] + 2);
	        }
	        else{
	        	cnt[2] = INT_MAX;
			}
			
			if((input - 2) % 3 == 0){
				cnt[3] = makeOne((input - 2)/3, cnt[3] + 3);
			}
			else{
				cnt[3] = INT_MAX;
			}
			
			if((input - 1) % 2 == 0){
				cnt[4] = makeOne((input - 1)/2, cnt[4] + 2);
			}
			else{
				cnt[4] = INT_MAX;
			}
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
