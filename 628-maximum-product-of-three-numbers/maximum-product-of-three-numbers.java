class Solution {
    public int maximumProduct(int[] nums) {
        int m1 = Integer.MIN_VALUE,m2 = Integer.MIN_VALUE,m3=Integer.MIN_VALUE;
        int min1=Integer.MAX_VALUE, min2= Integer.MAX_VALUE;
        for(int n:nums){
            if(n>m1){
                m3=m2;
                m2=m1;
                m1=n;
            }
            else if(n>m2){
                m3=m2;
                m2=n;
            }
            else if(n>m3){
                m3=n;
            }
            if(n<min1){
                min2=min1;
                min1=n;
            }
            else if(n<min2){
                min2=n;
            }
        }
        return Math.max(m1*m2*m3, min1*min2*m1);
    }
}