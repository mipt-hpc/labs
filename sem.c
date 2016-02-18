#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <linux/types.h>
#include <linux/ipc.h>
#include <linux/sem.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
  /* IPC */
  pid_t pid;
  key_t key;
  int semid;
  union semun arg;
  struct sembuf lock_res = {0, -1, 0};
  struct sembuf rel_res = {0, 1, 0};
  struct sembuf push[2] = {1, -1, IPC_NOWAIT, 2, 1, IPC_NOWAIT};
  struct sembuf pop[2] = {1, 1, IPC_NOWAIT, 2, -1, IPC_NOWAIT};

  /* Остальное */
  int i;

  if(argc < 2){
    printf("Usage: bufdemo [dimensione]\n");
    exit(0);
  }

  /* Семафоры */
  key = ftok("/etc/fstab", getpid());

  /* Создать набор из трёх семафоров */
  semid = semget(key, 3, 0666 | IPC_CREAT);

  /* Установить в семафоре номер 0 (Контроллер ресурсов)
     значение "1" */
  arg.val = 1;
  semctl(semid, 0, SETVAL, arg);

  /* Установить в семафоре номер 1 (Контроллер свободного места)
     значение длины буфера */
  arg.val = atol(argv[1]);
  semctl(semid, 1, SETVAL, arg);

  /* Установить в семафоре номер 2 (Контроллер элементов в буфере)
     значение "0" */
  arg.val = 0;
  semctl(semid, 2, SETVAL, arg);

  /* Fork */
  for (i = 0; i < 5; i++){
    pid = fork();
    if (!pid){
      for (i = 0; i < 20; i++){
        sleep(rand()%6);
        /* Попытаться заблокировать ресурс (семафор номер 0) */
        if (semop(semid, &lock_res, 1) == -1){
          perror("semop:lock_res");
        }
        /* Уменьшить свободное место (семафор номер 1) /
           Добавить элемент (семафор номер 2) */
        if (semop(semid, &push, 2) != -1){
          printf("---> Process:%d\n", getpid());
        }
        else{
          printf("---> Process:%d  BUFFER FULL\n", getpid());
        }
        /* Разблокировать ресурс */
        semop(semid, &rel_res, 1);
      }
      exit(0);
    }
  }

  for (i = 0;i < 100; i++){
    sleep(rand()%3);
    /* Попытаться заблокировать ресурс (семафор номер 0)*/
    if (semop(semid, &lock_res, 1) == -1){
      perror("semop:lock_res");
    }
    /* Увеличить свободное место (семафор номер 1) /
       Взять элемент (семафор номер 2) */
    if (semop(semid, &pop, 2) != -1){
      printf("<--- Process:%d\n", getpid());
    }
    else printf("<--- Process:%d  BUFFER EMPTY\n", getpid());
    /* Разблокировать ресурс */
    semop(semid, &rel_res, 1);
  }

  /* Удалить семафоры */
  semctl(semid, 0, IPC_RMID);

  return 0;
}
