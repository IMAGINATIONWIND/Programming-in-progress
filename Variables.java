import java.util.*;

public class Variables {
    public static void main(String[] args) {
        // System.out.print("Hello world");
        // System.out.println("println prints stuff in a new line");
        // System.out.println("Now we can see the difference");

        /*int a = 25;
        int b = 50;
        int sum = a + b ;
        System.out.println(sum);

        int mul = a * b ;
        System.out.println(mul);*/

        Scanner sc = new Scanner(System.in);
        String name = sc.next();
        // "next" takes only 1 token
        System.out.println(name);
        // HERE WE ARE CLEARING THE BUFFER SPACE
        sc.nextLine();
        String name2 = sc.nextLine();
        System.out.println(name2);
        


    }
}
