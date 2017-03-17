#include <stdio.h>

typedef unsigned char uint8;
typedef unsigned int  uint32;
typedef long long     uint64;

uint32 value_temp0[1000]={0};
uint32 value_temp1[1000]={0};
uint32 value_sum[1000]={0};

void array_plus()
{
    for (int i = 0; i < 1000; ++i)
    {
    	value_sum[i]=value_temp0[i]+value_temp1[i];
    }


    for (int i = 0; i < 1000; ++i)
    {
    	if (value_sum[i]>9)
    	{
    		value_sum[i+1]=value_sum[i+1]+value_sum[i]/10;
    		value_sum[i]=value_sum[i]%10;

    	}
    }
}

void print_sum(uint64 index)
{
	printf("no.%lld: ", index);
	for (uint32 i = 999; i >=1; --i)
	{
		printf("%ld", value_sum[i]);
	}
	printf("%ld", value_sum[0]);

	printf("\n");
}

int main(int argc, char *argv[])
{
	value_temp0[0]=1;
	value_temp1[0]=1;

	for (uint64 i = 1; i < 10000; ++i)
	{
		// value_sum=value_temp0+value_temp1;
		array_plus();

		// printf("%lld %lld\n",i+2, value_sum);
		
		print_sum(i+2);
		if (value_sum[999]>0)
		{
			print_sum(i+2);
			return 0;
		}
		// value_temp0=value_temp1;
		// value_temp1=value_sum;

		for (uint64 j = 0; j < 1000; ++j)
		{
			value_temp0[j]=value_temp1[j];
		}

		for (uint64 k = 0; k < 1000; ++k)
		{
			value_temp1[k]=value_sum[k];
		}

	}
	


}
