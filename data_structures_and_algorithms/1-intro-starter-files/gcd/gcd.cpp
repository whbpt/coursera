#include <iostream>
int min_max(int &a,int &b){
	int temp;
    if (b<a)
    {
		temp=a;
		a=b;
		b=temp;
	}
}


int gcd(int a, int b) {
	//write your code here
	int current_gcd = 1;
	while (b%a!=0)
	{
		min_max(a,b);
		b=b-a;
	}
	current_gcd=a;
  return current_gcd;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << gcd(a, b) << std::endl;
  return 0;
}
