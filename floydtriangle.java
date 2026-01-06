package patterns;

import java.util.Scanner;

public class floydtriangle {
        public static void main(String[] args){
        try(Scanner sc = new Scanner(System.in)){

        System.out.print("Enter the number of rows : ");
        int rows = sc.nextInt();
        // System.out.print("Enter the number of columns : ");
        // int columns = sc.nextInt();
        // int k = 0 ;
        for(int i = 1 ; i <= rows; i++){
        for(int j = 1 ; j <= i; j++){
            if ((i+j)%2 == 0){
                System.out.print(1);                
            }
            else{
                System.out.print(0);                
            }
            }
            System.out.println();
        }
}
}
}