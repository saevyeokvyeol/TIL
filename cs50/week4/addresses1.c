#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p; // *: int's address NOT int!
    p = &n; // &: get n's address

    printf("%i\n", n);
    printf("%p\n", &n);
    printf("%p\n", p); // If you want to print the address stored in p, there is no need for *
    printf("%i\n", *p);
}