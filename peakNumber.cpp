#include<bits/stdc++.h>
using namespace std;


int main()
{
	int N;
	scanf("%d",&N);
	int A[N];

	for(int i=0;i<N;i++)
	{
		scanf("%d",&A[i]);
	}
	int peak=A[0];
	for(int i=0;i<N;i++)
	{
		if(A[i]>peak)
		{
			peak=A[i];
		}
	}
	printf("Peak = %d\n",peak);

	return 0;
}