#include <stdio.h>

typedef unsigned char uint8;
typedef unsigned int  uint32;
typedef long long     uint64;

uint32 array[15][15]={{75},
       				    {95,64},
       				    {17,47,82},
       				    {18,35,87,10},
       				    {20, 4,82,47,65},
       				    {19, 1,23,75, 3,34},
       				    {88, 2,77,73, 7,63,67},
       				    {99,65, 4,28, 6,16,70,92},
       				    {41,41,26,56,83,40,80,70,33},
       				    {41,48,72,33,47,32,37,16,94,29},
       				    {53,71,44,65,25,43,91,52,97,51,14},
       				    {70,11,33,28,77,73,17,78,39,68,17,57},
       				    {91,71,52,38,17,14,91,43,58,50,27,29,48},
       				    {63,66, 4,68,89,53,67,30,73,16,69,87,40,31},
       				    {04,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23}};

uint32 array_avg[15]={0};

uint64 sum_max=0;

void calculate(uint32 i, uint32 j, uint64 sum_val)
{
	if (i==14)
	{
		if (array[i][j]<array_avg[i]/2)
		{
			return;
		}

		sum_val+=array[i][j];

		if (sum_max<sum_val)
		{
			sum_max=sum_val;
		}

		// printf("i=%d j=%d  sum=%lld\n", i, j, sum_val);

		return;

	}

	if (i==0)
	{
		sum_val+=array[i][j];

		calculate(i+1, j, sum_val);
		calculate(i+1, j+1, sum_val);

		return;
		
	}
	else
	{
		if (array[i][j]<array_avg[i]/2)
		{
			return;
		}

		sum_val+=array[i][j];

		calculate(i+1, j, sum_val);
		calculate(i+1, j+1, sum_val);

		return;
	}
	
}


int main(int argc, char *argv[])
{
    

    for (int i = 0; i < 15; ++i)
    {
    	uint64 avg_val=0;
    	for (int j = 0; j <= i; ++j)
    	{
    		// printf("%d ", array[i][j]);
    		avg_val+=array[i][j];
    	}
    	array_avg[i]=(uint32)(avg_val/(i+1));
    	// printf("\n");
    }


    // for (int i = 0; i < 15; ++i)
    // {
    // 	printf("%d ", array_avg[i]);
    // }


    uint64 sum_val=0;

    calculate(0, 0, sum_val);


    printf("sum max = %lld\n", sum_max);

}