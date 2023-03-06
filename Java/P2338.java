package Java;
import java.math.BigInteger;
import java.util.Scanner;

public class P2338 {

    public static void main(String[] args) {
        BigInteger a, b;
        Scanner sc = new Scanner(System.in);
        a = sc.nextBigInteger();
        b=sc.nextBigInteger();
        BigInteger c=a.add(b),d=a.subtract(b),e=a.multiply(b);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);
        sc.close();
    }

}