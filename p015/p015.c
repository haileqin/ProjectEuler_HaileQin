#include <stdio.h>

long long index_val=0;

void calculate(int x,  int y, int max_val)
{
    if (x==max_val && y==max_val)
    {
    	index_val=index_val+1;

    	return;
    }

    int i = 0;

    for (i = 0; i < 2; ++i)
    {
    	if (i==0)
    	{
    		if (x<max_val)
    		{
    			calculate(x+1, y, max_val);
    		}
    		else
    		{
    			return;
    		}
    	}

    	if (i==1)
    	{
    		if (y<max_val)
    		{
    			calculate(x, y+1, max_val);
    		}
    		else
    		{
    			return;
    		}
    	}
    }
}

void max_number_matrix(int max_val)
{
	index_val=0;
	calculate(0, 0, max_val);
	printf("%dx%d: %lld\n", max_val, max_val, index_val*2);
	index_val=0;
}


int main(int argc, char *argv[])
{
    int i = 0;
    for (i = 2; i <= 20; ++i)
    {
     	max_number_matrix(i);
    } 

}