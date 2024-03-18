public class Solution {
    public bool IsPalindrome(int x) {
       int num = x;
        int x1 = num;
        bool y = false;
        int rem = 0;
        int rev = 0;
        if (num<0){
            return false;
        }
        while (num>0) {
            rem=num % 10;
            rev = rev*10 + rem;
            num =num / 10;
        }
        if (x1 == rev)
        {
            y = true;
        }
        else
        {
            y = false;
        }
        return y;
    }
}
