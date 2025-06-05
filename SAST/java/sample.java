public class Sample {
    public static void main(String[] args) {
        char[] password = "sensitivePassword".toCharArray();
        System.out.println("Received password: " + new String(password));
        Arrays.fill(password, ' ');
    }
}