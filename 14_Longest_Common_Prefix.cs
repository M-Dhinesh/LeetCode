public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        int minLength = strs.Min(y=>y.Length);
        string shortest = strs.FirstOrDefault(x=>x.Length == minLength);
        string result="";
        for (int i=0;i<minLength;i++){
            int c=1;
            foreach(string s in strs){
                if (s[i]!=shortest[i]){
                    c=0;
                    break;
                }
            }
            if (c==0){
                break;
            }
            else{
                result+=shortest[i];
            }
        }
        return result;
    }
}
