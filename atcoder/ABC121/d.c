#include <stdio.h>

int main(){
  long long A,B;
  long long ans = 0;
  long long i;
  scanf("%lld %lld", &A, &B);
  for(i=A;i<B+1;++i){
    ans ^= i;
  }
  printf("%lld\n", ans);
}
