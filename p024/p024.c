#include <stdio.h>

typedef unsigned char uint8;
typedef unsigned int  uint32;
typedef long long     uint64;



int main(int argc, char *argv[])
{

	uint64 index=0;

    for (int i_0 = 0; i_0 < 10; ++i_0)
    {
    	for (int i_1 = 0; i_1 < 10; ++i_1)
	    {
	    	if (i_1==i_0)
	    	{
	    		continue;
	    	}
	    	for (int i_2 = 0; i_2 < 10; ++i_2)
		    {
		    	if (i_2==i_0 || i_2==i_1)
		    	{
		    		continue;
		    	}
		    	for (int i_3 = 0; i_3 < 10; ++i_3)
			    {
			    	if (i_3==i_0 || i_3==i_1 || i_3==i_2)
			    	{
			    		continue;
			    	}
			    	for (int i_4 = 0; i_4 < 10; ++i_4)
				    {
				    	if (i_4==i_0 || i_4==i_1 || i_4==i_2 || i_4==i_3)
				    	{
				    		continue;
				    	}
				    	for (int i_5 = 0; i_5 < 10; ++i_5)
					    {
					    	if (i_5==i_0 || i_5==i_1 || i_5==i_2 || i_5==i_3 || i_5==i_4)
					    	{
					    		continue;
					    	}
					    	for (int i_6 = 0; i_6 < 10; ++i_6)
						    {
						    	if (i_6==i_0 || i_6==i_1 || i_6==i_2 || i_6==i_3 || i_6==i_4 || i_6==i_5)
						    	{
						    		continue;
						    	}
						    	for (int i_7 = 0; i_7 < 10; ++i_7)
							    {
							    	if (i_7==i_0 || i_7==i_1 || i_7==i_2 || i_7==i_3 || i_7==i_4 || i_7==i_5 || i_7==i_6)
							    	{
							    		continue;
							    	}
							    	for (int i_8 = 0; i_8 < 10; ++i_8)
								    {
								    	if (i_8==i_0 || i_8==i_1 || i_8==i_2 || i_8==i_3 || i_8==i_4 || i_8==i_5 || i_8==i_6 || i_8==i_7)
								    	{
								    		continue;
								    	}
								    	for (int i_9 = 0; i_9 < 10; ++i_9)
									    {
									    	if (i_9==i_0 || i_9==i_1 || i_9==i_2 || i_9==i_3 || i_9==i_4 || i_9==i_5 || i_9==i_6 || i_9==i_7 || i_9==i_8)
									    	{
									    		continue;
									    	}

									    	index++;

									    	if (index==1000000)
									    	{
									    		printf("no.%lld: %d%d%d%d%d%d%d%d%d%d \n", index, i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8, i_9 );
									    		return 0;
									    	}
									    	
									    }
								    }
							    }
						    }
					    }
				    }
			    }
		    }
	    }
    }	


}
