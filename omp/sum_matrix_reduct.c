#include <omp.h>
#include <stdlib.h>
#include <stdio.h>
#define CHUNK 100 
#define NMAX 1000 
#define LIMIT 100
main () { 
 int i, j, sum; 
 int a[NMAX][NMAX]; 
 srand ( time(NULL) );
 for (i=0;i<NMAX;i++){
	for (j=0; j < NMAX; j++){
		a[i][j] = 1; //rand() % 10
	}
 }

int total = 0; 
#pragma omp parallel for shared(a) private(i,j,sum) reduction (+:total) 
 
  for (i=0; i < NMAX; i++) { 
    sum = 0; 
    for (j=0; j < NMAX; j++) 
      sum += a[i][j]; 
    printf ("Сумма строки %d равна %d\n",i,sum); total = total + sum; 
} /* Завершение параллельного фрагмента */ 

printf ("Общая сумма матрицы равна %d\n",total);
}
