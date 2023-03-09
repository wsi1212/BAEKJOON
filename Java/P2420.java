package Java;
import java.util.Scanner;

public class P2420 {

    public static void main(String[] args) {
        long a=0, b=0;
        Scanner sc = new Scanner(System.in);
        a = sc.nextLong();
        b=sc.nextLong();
        if(a>=b)
        System.out.println(a-b);
        else
        System.out.println(b-a);
    }

}