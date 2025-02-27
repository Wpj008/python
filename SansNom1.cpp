#include<stdio.h>
#include<stdlib.h>

int main(){
	
	
	int i; int j ; int k ; int s = 0 ;
	
	
	for(i = 1 ; i<3 ; i++){
		
		for(j = 1 ; j<50 ; j++){
			
			for(k = 1 ; k<12 ; k++){
				
				s = s+1;
			}
		}
		
		
	}
	
	
	printf("%d", s);
	
	
	return 0;
}
