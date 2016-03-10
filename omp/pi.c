#include <stdio.h>
static long num_steps = 10000000; 
long double step; 
int main () 
{ 
	int i; 
	long double x, pi, sum = 0.0; 
	step = 1.0/(long double) num_steps; 
	for (i=0;i<= num_steps; i++){ 
		x = (i+0.5)*step; 
		sum = sum + 4.0/(1.0+x*x); 
	} 
	pi = step * sum; 
	printf("%Lf\n",pi);
} 

