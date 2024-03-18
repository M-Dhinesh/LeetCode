using System.Text.RegularExpressions;
public class Solution {
    public bool IsMatch(string s, string p) {
        return Regex.IsMatch(s,"^"+p+"$");
    }
}
