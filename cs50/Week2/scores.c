#include <cs50.h>
#include <stdio.h>

const int N = 3;

float average(int array[]);

int main(void)
{
    // int score1 = 72;
    // int score2 = 73;
    // int score3 = 33;

    // printf("Average: %f\n", (score1 + score2 + score3) / (float) 3);

    // int scores[n];

    // scores[0] = get_int("Score1: ");
    // scores[1] = get_int("Score2: ");
    // scores[2] = get_int("Score3: ");

    int scores[N];

    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score%i: ", i + 1);
    }

    printf("Average: %f\n", average(scores));
}

float average(int array[])
{
    int sum = 0;

    for (int i = 0; i < N; i++)
    {
        sum += array[i];
    }

    return sum / (float) 3;
}