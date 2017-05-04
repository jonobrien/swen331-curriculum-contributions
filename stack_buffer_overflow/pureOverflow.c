#include <stdlib.h>
#include <stdio.h>
#include <string.h>


void boom() {
    printf("BOOM\n");
}

int main(int argc, char **argv) {
    char buffer[64];
    gets(buffer);
    printf("%s\n",buffer);
}

