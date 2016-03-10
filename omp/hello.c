#include <stdio.h>
#include <omp.h>
main () {
  /* Выделение параллельного фрагмента*/
#pragma omp parallel
  { printf("Hello World !\n");
  }/* Завершение параллельного фрагмента */
}
