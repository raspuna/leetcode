import java.util.Arrays;

public class P26 {
    public void swap(int[] nums, int idx1, int idx2) {
        int tmp = nums[idx1];
        nums[idx1] =nums[idx2];
        nums[idx2] = tmp;
    }
    public void sort(int[] nums) {
        for (int i = 0; i < nums.length-1; i++) {
            for (int j = 0; j < nums.length -1 -i;j++) {
                if (nums[j] > nums[j+1]) {
                    swap(nums, j, j+1);
                }
            }

            System.out.println(Arrays.toString(nums));
        }
        System.out.println(Arrays.toString(nums));
    }
    public int removeDuplicates1(int[] nums) {
        int k = 0;
        if(nums.length < 2){
            return nums.length;
        }
        int i = 0;
        while(i < nums.length - 1 - k) {
            System.out.printf("%d (%d, %d):", i, nums[i], nums[i+1]);
            if (nums[i] == nums[i+1]) {
                k++;
                nums[i+1] = 200;
                for(int j = i+1; j< nums.length-k; j++){
                    swap(nums, j, j+1);
                }
                System.out.println(Arrays.toString(nums));
            } else {
                i++;
            }
        }
        System.out.println(Arrays.toString(nums));
        return nums.length - k;
    }
    public int removeDuplicates2(int[] nums) {
        int k = 0;
        if(nums.length < 2){
            return nums.length;
        }


        int i = nums.length - 1;
        while(i > 0) {
            //System.out.printf("%d (%d, %d):", i, nums[i-1], nums[i]);
            if (nums[i-1] == nums[i]) {
                k++;
                for(int j = i; j< nums.length-k; j++){
                    swap(nums, j, j+1);
                }
                //System.out.println(Arrays.toString(nums));
            } 
            i--;
            //System.out.println("");
        }
        //System.out.println(Arrays.toString(nums));
        return nums.length - k;
    }
    // solution
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
            System.out.printf("i:%d, j:%d %s\n", i, j, Arrays.toString(nums));
        }
        return i + 1;
    }
    public static void main(String[] args) {
        int[] a = {0,0,1,1,1,2,2,3,3,4};
        //int[] a = {1,2};
        P26 p = new P26();
        p.removeDuplicates(a);

    }
}
