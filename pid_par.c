#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
  pid_t pid;
  int i;

  pid = fork();

  if (pid == 0){
    for (i = 0; i  < 8; i++){
      printf("-ДОЧЕРНИЙ-\n");
    }
    return(0);
  }

  for (i = 0; i < 8; i++){
    printf("+РОДИТЕЛЬСКИЙ+\n");
  }

  return(0);
}
