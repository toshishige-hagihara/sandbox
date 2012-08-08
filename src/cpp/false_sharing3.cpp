#include <stdio.h>
#include <pthread.h>
#include <time.h>
#include <sys/time.h>
#include <sys/resource.h>

int counts = 20000000;
int counts2 = 20000000;

struct c{
    int c1;
    int c2;
} counters;

struct c2{
    int c1[16];
    int c2[16];
} counters2;

clock_t f_start;
clock_t f_end;
double f_et;

clock_t g_start;
clock_t g_end;
double g_et;

double get_elapsed_time

void* f(void *arg) {
    for(int i=0; i < counts; i++){
        __sync_fetch_and_add((int *)arg, 1);
    }

    struct rusage usage;
    getrusage(RUSAGE_THREAD, &usage);
    f_et = (double)usage.ru_utime.tv_sec + (double)usage.ru_utime.tv_usec/1000000.0;
    return NULL;
}

void* g(void *arg) {
    g_start = clock();
    for(int i=0; i < counts2; i++){
        __sync_fetch_and_add((int *)arg, 1);
    }

    g_end = clock();
    return NULL;
}

int main(void)
{
    pthread_t t_f;
    pthread_t t_g;
    clock_t start;
    clock_t end;
    struct rusage usage;

    printf("***** parallel *****\n");

    start = clock();
    pthread_create(&t_f, NULL, f, &counters.c1);
    pthread_create(&t_g, NULL, g, &counters.c2);
    pthread_join(t_f, NULL);
    pthread_join(t_g, NULL);
    end = clock();
    getrusage(RUSAGE_SELF, &usage);
    printf("[same cache line] %lf sec\n", (double)usage.ru_utime.tv_sec + (double)usage.ru_utime.tv_usec/1000000.0);
    printf("[same cache line: f] %lf sec\n", (double)(f_end - f_start)/CLOCKS_PER_SEC);
    printf("[same cache line: g] %lf sec\n", (double)(g_end - g_start)/CLOCKS_PER_SEC);

    start = clock();
    pthread_create(&t_f, NULL, f, &counters2.c1[0]);
    pthread_create(&t_g, NULL, g, &counters2.c2[0]);
    pthread_join(t_f, NULL);
    pthread_join(t_g, NULL);
    end = clock();

    printf("[different cache line] %f sec\n", (double)(end - start)/CLOCKS_PER_SEC);
    printf("[different cache line: f] %f sec\n", (double)(f_end - f_start)/CLOCKS_PER_SEC);
    printf("[different cache line: g] %f sec\n", (double)(g_end - g_start)/CLOCKS_PER_SEC);

    printf("***** serial *****\n");

    start = clock();
    pthread_create(&t_f, NULL, f, &counters.c1);
    pthread_join(t_f, NULL);

    pthread_create(&t_g, NULL, g, &counters.c2);
    pthread_join(t_g, NULL);
    end = clock();

    printf("[same cache line] %f sec\n", (double)(end - start)/CLOCKS_PER_SEC);
    printf("[same cache line: f] %f sec\n", f_et);
    printf("[same cache line: g] %f sec\n", (double)(g_end - g_start)/CLOCKS_PER_SEC);

    start = clock();
    pthread_create(&t_f, NULL, f, &counters2.c1[0]);
    pthread_join(t_f, NULL);

    pthread_create(&t_g, NULL, g, &counters2.c2[0]);
    pthread_join(t_g, NULL);
    end = clock();

    printf("[different cache line] %f sec\n", (double)(end - start)/CLOCKS_PER_SEC);
    printf("[different cache line: f] %f sec\n", f_et);
    printf("[different cache line: g] %f sec\n", (double)(g_end - g_start)/CLOCKS_PER_SEC);

    return 0;
}
