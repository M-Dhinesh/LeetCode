public class Solution {
    public int[] TwoSum(int[] nums, int target) {
            int loopbreak = 0;
            int[] sol = new int[2];
            for ( int i=0; i<nums.Length; i++ )
            {
                for ( int  j=0; j<nums.Length; j++ )
                {
                    if ( i != j )
                    {
                        if (nums[i] + nums[j] == target)
                        {
                            sol[0]=i;
                            sol[1]=j;
                            loopbreak++;
                            break;
                        }
                    }
                }
                if (loopbreak == 1){break;}
            }
            return sol;
    }
}
