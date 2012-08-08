#include <stdio.h>
#include <pthread.h>
#include <time.h>

int counts = 20000000;

struct c{
    int c1;
    int c2;
} counters;

struct c2{
    int c1[16];
    int c2[16];
} counters2;

void* f(void *arg) {
    for(int i=0; i < counts; i++){
        __sync_fetch_and_add((int *)arg, 1);
    }

    return NULL;
}

void* g(void *arg) {
    for(int i=0; i < counts; i++){
        __sync_fetch_and_add((int *)arg, 1);
    }

    return NULL;
}

int main(void)
{
    pthread_t t_f;
    pthread_t t_g;
    clock_t start;
    clock_t end;

    printf("***** parallel *****\n");

    start = clock();
    pthread_create(&t_f, NULL, f, &counters.c1);
    pthread_create(&t_g, NULL, g, &counters.c2);
    pthread_join(t_f, NULL);
    pthread_join(t_g, NULL);
    end = clock();

    printf("[same cache line] %f sec\n", (double)(end - start)/CLOCKS_PER_SEC);

    start = clock();
    pthread_create(&t_f, NULL, f, &counters2.c1[0]);
    pthread_create(&t_g, NULL, g, &counters2.c2[0]);
    pthread_join(t_f, NULL);
    pthread_join(t_g, NULL);
    end = clock();

    printf("[different cache line] %f sec\n", (double)(end - start)/CLOCKS_PER_SEC);

    printf("***** serial *****\n");

    start = clock();
    pthread_create(&t_f, NULL, f, &counters.c1);
    pthread_join(t_f, NULL);

    pthread_create(&t_g, NULL, g, &counters.c2);
    pthread_join(t_g, NULL);
    end = clock();

    printf("[same cache line] %f sec\n", (double)(end - start)/CLOCKS_PER_SEC);

    start = clock();
    pthread_create(&t_f, NULL, f, &counters2.c1[0]);
    pthread_join(t_f, NULL);

    pthread_create(&t_g, NULL, g, &counters2.c2[0]);
    pthread_join(t_g, NULL);
    end = clock();

    printf("[different cache line] %f sec\n", (double)(end - start)/CLOCKS_PER_SEC);

    return 0;
}
