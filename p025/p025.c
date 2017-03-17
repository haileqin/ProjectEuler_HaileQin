#include <stdio.h>

typedef unsigned char uint8;
typedef unsigned int  uint32;
typedef long long     uint64;

uint32 array[1000]={0};
uint32 array_temp[1000]={0};
uint32 array_sum[1000]={0};

int main(int argc, char *argv[])
{
	uint64 value_temp0=1;
	uint64 value_temp1=1;
	uint64 value_sum=0;

	for (uint64 i = 1; i < 15; ++i)
	{
		value_sum=value_temp0+value_temp1;
		printf("%lld %lld\n",i+2, value_sum);
		value_temp0=value_temp1;
		value_temp1=value_sum;
	}
	


}
