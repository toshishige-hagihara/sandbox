int main(void)
{
    int a1=0;
//    a1++;
    __sync_add_and_fetch(&a1, 1);
    __sync_synchronize();
}
