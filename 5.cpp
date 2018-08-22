//错误！！！！
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
char c[10010];
char* longestPalindrome(char* s) {
    int n = strlen(s), ans = 0, l, r, mx;
    
    for(int i = 0; i < n; i++){
        mx = i > (n -i) ? i : n - i;
        int p = 0;
        for(int j = 0; j < mx; j++){
            if(s[i - j] == s[i + j])p++;
            else break;
           }
        if(p > ans){
            ans = p;
            l = i - mx + 1, r = i + mx - 1;
            }
    }   
    int tot = 0;
    for(int i = l; i <= r; i++)c[++tot] = s[i];
    printf("%s", c);
    return 0;
    }
int main(){
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    char s[10010];
    scanf("%s", s);
    longestPalindrome(s);
    
}
