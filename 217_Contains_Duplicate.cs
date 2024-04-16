public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        var hash=new HashSet<int>();
        foreach (var item in nums)
            if (!hash.Add(item)) 
                return true;
        return false;
    }
}
