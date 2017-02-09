#include <stdio.h>

long long sum_prime=2;


long long prime_judge(long long index,long long max_index,long long value)
{
    if (index>=max_index)
    {
    	sum_prime=sum_prime+value;
        return;
    }

    if (value%index!=0)
    {
    	prime_judge(index+1, value/index, value);
    }
    else
    {
    	return;
    }
}

int main(int argc, char *argv[])
{

    long long i;
    for (i = 3; i < 2000000; ++i)
    {
    	if (i%10000==0)
    	{
    		printf("%lld  %lld\n", i, sum_prime);
    	}

    	prime_judge(2, i, i);
    }

    printf("%lld\n", sum_prime);
}