public class P28 {
    public int strStr(String haystack, String needle) {
        for(int i = 0; i< haystack.length(); i++ ){
            if (haystack[i] == needle[0]) {
                for(int j=0; j<needle.length(); j++){
                    if(haystack[i+j] != needle[j]) {
                        break;
                    }
                }
            }
        }
    }   
    public static void main(String[] args) {
        P28 myP = new P28();
        System.out.println(myP.strStr("hello", "ll"));
        System.out.println(myP.strStr("aaaaa", "bba"));
        System.out.println(myP.strStr("", ""));
    }
}
