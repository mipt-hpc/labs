#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

int main()
{
  pid_t pid;
  int i;

  pid = fork();

  if (pid == 0){
    for (i = 0; i < 14; i++){
      sleep (rand()%4);
      printf("-ДОЧЕРНИЙ-\n");
    }
    return 0;
  }

  sleep (rand()%4);
  printf("+РОДИТЕЛЬСКИЙ+ Ожидаю завершения выполнения дочернего процесса...\n");
  waitpid (pid, NULL, 0);
  printf("+РОДИТЕЛЬСКИЙ+ ...завершен\n");

  return 0;
}
