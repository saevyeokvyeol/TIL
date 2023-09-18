#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // ...

    // int *tmp = malloc(4 * sizeof(int));

    // for (int i = 0; i < 3; i++)
    // {
    //     tmp[i] = list[i];
    // }
    // tmp[3] = 4;

    // free(list);

    int *tmp = realloc(list, 4); // reallock does lines 18-26 instead of me
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }

    list = tmp;
    list[3] = 4;

    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    free(list);
    return 0;
}