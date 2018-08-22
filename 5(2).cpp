class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size() == 0)return "";
        int i = 0, j = 0;
        int n = s.size();
        bool p[n][n] = {false};
        for(int i = 0; i < n; i++){
            p[i][i] = true;
            if(i == n-1)break;
            p[i][i+1] = (s[i] == s[i+1]);
        }
        for(int i = n - 3; i >= 0; i--){
            for(int j = i+2; j < n; j++)
                p[i][j] = (p[i+1][j-1] && s[i] == s[j]);
        }
        int mx = 0;
        string ans = "";
        for(int i = 0; i < n; i++){
            for(int j = i; j < n; j++){
                if(p[i][j] == true&&j-i+1 > mx){
                    mx = j-i+1;
                    ans = s.substr(i, j-i+1);
                }
            }
        }
        return ans;
    }
};