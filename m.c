#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define SUCESSO 0

int main(){
    srand(time(NULL));

    printf("\033[1;32m");

    printf("\U0001F5200");
    getchar();
    while(1){
        for(int i=0;i<180;i++){
            if((rand() % 5) == 1){
                printf("%d", rand() % 10);
            }
            else
                printf(" ");
                usleep(100);
        }
        printf("\n");
    }

    return SUCESSO;
}
