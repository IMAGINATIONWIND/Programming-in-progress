package patterns.Advanced_patterns;
import java.util.*;
public class numberpyramid {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)){

        System.out.print("Enter number of rows : ");
        int rows = sc.nextInt();
        int l = 0;
        for (int i = rows ; i >= 1; i--){

            l = l+1;

            for
             (int j = 2 ;j <= i ; j++ ){
                System.out.print(" ");
            }
                for (int k = 1 ;k <= l ; k++ ){
                         System.out.print(l);
                         System.out.print(" ");
            }
            System.out.println();
        }
            System.out.println();
    }
}
}