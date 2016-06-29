#include <iostream>
#include <vector>
using namespace std;
long long get_fibonaccihuge(long long n, long long m) {
  //write your code here
    vector<long long> fff;
	long long p,mm;
	if (n<=1)
        return n;
	if (n>m*m)
	{
		mm=m*m;
	}
	else
	{
		mm=n;
	}
	fff.assign(mm+1,0);
	fff[1]=1;
	{
    	for(int i=2;i!=mm+1;i++)
		{
			fff[i]=(fff[i-1]+fff[i-2])%m;
    		if (fff[i]==1&&fff[i-1]==0)
			{
				p=i-1;
				return fff[n%p];
			}
		}
	}
    return fff[n];
}

int main() {
    long long n, m;
    std::cin >> n >> m;
    std::cout << get_fibonaccihuge(n, m) << '\n';
}
