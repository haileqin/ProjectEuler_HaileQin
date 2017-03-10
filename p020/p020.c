#include <stdio.h>

typedef unsigned char uint8;
typedef unsigned int  uint32;
typedef long long     uint64;

uint32 array[10000]={0};

void print_sum(uint32 index)
{

	uint64 sum_val=0;
	for (uint64 i = 0; i < 10000; ++i)
	{
		sum_val=sum_val+array[i];
	}

	printf("%d factorial => %lld\n", index, sum_val);

    int lock=0;

    for (uint64 i = 9999; i >=0; --i)
    {
    	if (lock==0 && array[i]==0)
    	{
    		continue;
    	}

    	if (lock==1)
    	{
    		printf("%d", (uint32)(array[i]));
    		continue;
    	}


    	if (array[i]!=0)
    	{
    		printf("%d", (uint32)(array[i]));
    		lock=1;
    		continue;
    		
    	}
    }

    printf("\n");
	
}


int main(int argc, char *argv[])
{

	uint32 factorial_number=100;

	array[0]=1;

	uint32 temp=0;

	for (uint32 i = 0; i < factorial_number; ++i)
	{
		for (uint32 j = 0; j < 10000; ++j)
		{
    	    array[j]=array[j]*(i+1);   	    
		}


		for (uint32 j = 0; j < 10000; ++j)
		{
			temp=0;
			temp = array[j];

			if (array[j]<10)
	    	{
	    		continue;
	    	}
	    	else
	    	{
	    		array[j]=temp%10;

	    		temp=temp/10;

	    		uint32 x;

	    		for (x = j+1; x < 10000; ++x)
	    		{
	    			if (array[x]+temp>=10)
	    			{
	    				temp=array[x]+temp;
	    				array[x]=temp%10;
	    				temp=temp/10;
	    				// printf("%d ", (uint32)(temp));
	    			}
	    			else
	    			{
	    				array[x]=array[x]+temp;
	    				temp=0;
	    				break;
	    			}
	    		}
	    	}
		}
		

    print_sum(i+1);
	}


}
