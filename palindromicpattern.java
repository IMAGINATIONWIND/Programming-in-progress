package patterns.Advanced_patterns;
import java.util.*;
public class palindromicpattern {
    public static void main(String[] args) {
        try(Scanner sc = new Scanner(System.in)){
        
        System.out.print("Enter number of rows : ");
        int rows = sc.nextInt();
        int l = 0;
        int c = 2;
        for (int i = rows ; i >= 1; i--){
            int p = 0;
            l = l+1;
            
            for
            (int j = 2 ;j <= i ; j++ ){
                System.out.print("  ");
            }
            if (l>=2){
                // System.out.print(c);
                for (int b = c; b>=2 ; b-- ) {
                        System.out.print(b+" ");
                    }
                c = c+1;
                    }
            for (int k = 1 ;k <= l ; k++ ){
                p = p+1;
                         System.out.print(p+" ");
            }
            System.out.println();
        }
            System.out.println();
    }
}
}