#include<bits/stdc++.h>
using namespace std;

int counter=0;

int peakFinder(int a[],int start,int end);

int main()
{
	int N;
	scanf("%d",&N);
	int A[N];

	for(int i=0;i<N;i++)
	{
		scanf("%d",&A[i]);
	}

	int peak=peakFinder(A,0,N-1);

	printf("The peak is : %d\n",peak);
	printf("Approaches needed = %d\n",counter);
	return 0;
}

int peakFinder(int a[],int start,int end)
{
	counter++;
	int mid=(start+end+1)/2;

	if((a[mid]>a[mid+1]&&mid==start)||(a[mid]>a[mid+1]&&mid==end))
	{
		return a[mid];
	}
	else if((a[mid]>a[mid-1])&&(a[mid]>a[mid+1]))
	{
		return a[mid];
	}
	else if(a[mid]<a[mid-1])
	{
		return peakFinder(a,start,mid-1);
	}
	else if(a[mid]<a[mid+1])
	{
		return peakFinder(a,mid+1,end);
	}
}