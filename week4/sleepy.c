#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
// #include <windows.h>


int main(int argc, char *argv[]){
    int sleepTime = atoi(argv[1]);
    sleep(sleepTime);
    printf("Awake\n");
    return 0;
}
