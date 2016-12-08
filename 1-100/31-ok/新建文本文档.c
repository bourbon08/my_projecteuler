#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(void) {
    int n; 
    scanf("%d",&n);
    int arr[n];
    for(int arr_i = 0; arr_i < n; arr_i++){
       scanf("%d",&arr[arr_i]);
    }    
    
    for(int arr_i = 0; arr_i < n; arr_i++){
	   int m = arr[arr_i];
	   int c[] = {1,2,5,10,20,50,100,200};
	   int a[m], b[m];
	   int d = 8;
    
       b[0]=1;     
	   for(int i = 1; i <= m; i++) {
	       b[i] = 0;
	   }

	   for(int i = 0; i < d; i++) {
		  for(int j = c[i]; j <= arr[arr_i]; j++) {
			 b[j]=(b[j]+b[j-c[i]])%(1000000007);
		  }
	   }
	
	   printf("%d \n", b[arr[arr_i]]);
    }
    return 0;
	
}
