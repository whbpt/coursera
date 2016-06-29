#include <iostream>
long long min_max(long long &a,long long &b){
    long long temp;
    if (b<a)
    {
        temp=a;
        a=b;
        b=temp;
    }
}
long long gcd(long long a, long long b) {
    //write your code here
    long long current_gcd = 1;
    while (b%a!=0)
    {
        min_max(a,b);
        b=b%a;
    }
    current_gcd=a;
  return current_gcd;
}
long long lcm(long long a, long long b) {
	return a/gcd(a,b)*b;
}

int main() {
  long long a, b;
  std::cin >> a >> b;
  std::cout << lcm(a, b) << std::endl;
  return 0;
}
