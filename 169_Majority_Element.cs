public class Solution {
    public int MajorityElement(int[] nums) {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        
        foreach (var n in nums)
        {
            if (!dict.ContainsKey(n))
                dict.Add(n, 0);
            
            dict[n] += 1;
            
            if (dict[n] > nums.Length / 2)
                return n;
        }
        
        return -1;
    }
}
