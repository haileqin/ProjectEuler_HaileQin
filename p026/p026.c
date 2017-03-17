#include <stdio.h>

typedef unsigned char uint8;
typedef unsigned int  uint32;
typedef long long     uint64;


void calaulate(uint32 value)
{
    printf("%d : ", value);

	uint32 base_num=1;

	for (int i = 0; i < 10000; ++i)
	{
		if (base_num%value==0)
		{
			printf("%d", base_num/value);
			break;
		}
		
		if (base_num<value)
		{
			base_num=10*base_num;
			continue;
		}

		printf("%d", base_num/value);
		base_num=base_num%value;
	}

	printf("\n");

}


int main(int argc, char *argv[])
{

	for (int i = 2; i < 1000; ++i)
	{
		calaulate(i);
	}

}
