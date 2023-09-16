#include <stdio.h>

int main(void)
{
    char *s = "HI!";

    printf("%s\n", s);
    printf("\n");

    printf("%p\n", s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
    printf("\n");

    printf("%c\n", s[0]);
    printf("%c\n", s[1]);
    printf("%c\n", s[2]);
    printf("\n");

    printf("%c\n", *s);
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
    printf("\n");

    printf("%s\n", s);
    printf("%s\n", s + 1);
    printf("%s\n", s + 2);
}