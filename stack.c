
// gcc -fno-stack-protector -g -o stack stack.c

#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void win()
{
  printf("arbitrarily ran win()\n");
}

int main(int argc, char **argv)
{
  volatile int (*fp)();
  char buffer[64];

  fp = 0;

  gets(buffer);

  if(fp) {
      printf("invoking function, jmp to 0x%08x\n", fp);
      fp();
  }
}
