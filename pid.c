#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>

int main()
{
  pid_t pid;

  pid = getpid();
  printf("pid присвоенный процессу - %d\n", pid);

  return 0;
}
