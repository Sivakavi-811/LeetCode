class Solution {
    public int missingMultiple(int[] nums, int k) {
        HashSet<Integer> set = new HashSet<>();
        for(int n : nums){
            set.add(n);
        }
        int i;
        for(i=1;i<=set.size();i++){
            int p = i*k;
            if(!set.contains(p)){
                return p;
            }
        }

        return k*i;
    }
    
}