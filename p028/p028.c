#include <stdio.h>

typedef unsigned char uint8;
typedef unsigned int  uint32;
typedef long long     uint64;


int main(int argc, char *argv[])
{
	uint64 matrix_num=1001;
	uint64 distance=2;
	uint64 index=0;
	uint64 sum = 0;

	
	for (uint64 i = 1; i <= matrix_num*matrix_num; )
	{
		if (index==4)
		{
			index=0;
			distance=distance+2;
		}
		// printf("%lld\n", i);
		sum=sum+i;

        i=i+distance;
        index++;
	}

	printf("sum=%lld\n", sum);


}
