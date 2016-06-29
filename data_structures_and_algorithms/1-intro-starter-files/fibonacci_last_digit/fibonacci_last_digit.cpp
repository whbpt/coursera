#include <iostream>

int get_fibonacci_last_digit(int n) {
  //write your code here
    long long fff[3];
    fff[0]=0;fff[1]=1;fff[2]=1;
    int m(10);
	long long p,mm;
    if (n<=1)
        return n;
    mm=m*m;
    for(int i=2;i!=mm+1;i++)
    {
        p=mm+1;
        fff[2]=(fff[1]+fff[0])%m;
        if (fff[2]==0&&fff[1]==1)
        {
            p=i;
            break;
        }
        fff[0]=fff[1];fff[1]=fff[2];
    }
    for(int i=0;i!=(n%p)+1;i++)
    {
        fff[2]=(fff[1]+fff[0])%m;
        fff[0]=fff[1];fff[1]=fff[2];
    }
    return fff[2];

  return 0;
}

int main() {
  int n;
  std::cin >> n;
  int c = get_fibonacci_last_digit(n);
  std::cout << c << '\n';
}
