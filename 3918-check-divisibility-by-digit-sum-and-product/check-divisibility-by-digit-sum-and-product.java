class Solution {
    public boolean checkDivisibility(int n) {
        int temp = n;
        int sum=0;
        int prod=1;
        int total =0;

        while (temp>0){
            int t = temp % 10;
            sum += t;
            prod *= t;
            temp/=10;
        }
        total = sum + prod;
        return (n % total)== 0;
    }
}