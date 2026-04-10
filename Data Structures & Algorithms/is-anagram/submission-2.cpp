class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() == t.length()) {
            
            unordered_map <char, int> CountS;
            unordered_map <char, int> CountT;
            for (int i = 0; i < s.length(); i++) {
                CountS[s[i]]++;
                CountT[t[i]]++;
            }
            // return true if they are anagram
            return CountS == CountT;
        } else {
            return false;
            std::cout << "cannot be anagrams if length differs :)" <<endl;
        }
    }
};
