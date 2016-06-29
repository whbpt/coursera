#include <iostream>
#include <vector>
using namespace std;
int calc_fib(int n) {
	vector<long> fff;
	if (n<=1)
		return n;
	fff.assign(n+1,0);
	fff[0]=0;fff[1]=1;
	for(int i=2;i!=n+1;i++)
	{
		fff[i]=fff[i-1]+fff[i-2];
    }
	return fff[n];
}

int main() {
    int n = 0;
    std::cin >> n;

    std::cout << calc_fib(n) << '\n';
    return 0;
}
