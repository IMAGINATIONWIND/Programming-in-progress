package patterns.Advanced_patterns;
import java.util.*;
public class rhombus {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)){

        System.out.print("Enter number of rows : ");
        int rows = sc.nextInt();

        for (int i = rows ; i >= 1; i--){
            for (int j = 2 ;j <= i ; j++ ){
                System.out.print(" ");
            }
        for (int k = 1 ;k <= rows ; k++ ){
                System.out.print("*");
            }
        
            System.out.println();
        }
    }
}

}