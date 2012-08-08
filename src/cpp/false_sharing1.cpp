#include <stdio.h>
#include <pthread.h>
#include <time.h>

struct {
    int c1;
    int c2;
} counters;

void* f(void *args) {
    for(int i=0; i < 10000000; i++){
        __sync_fetch_and_add(&(counters.c1), 1);
    }
}

void* g(void *args) {
    for(int i=0; i < 10000000; i++){
        __sync_fetch_and_add(&(counters.c2), 1);
    }
}

int main(void)
{
    pthread_t t_f;
    pthread_t t_g;
    clock_t start;
    clock_t end;

    start = clock();
    pthread_create(&t_f, NULL, f, NULL);
    pthread_create(&t_g, NULL, g, NULL);

    pthread_join(t_f, NULL);
    pthread_join(t_g, NULL);
    end = clock();

    printf("total %f sec\n", (double)(end - start)/CLOCKS_PER_SEC);
}
