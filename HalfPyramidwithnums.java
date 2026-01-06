package patterns;

import java.util.*;

public class HalfPyramidwithnums {
    public static void main(String[] args){
        try(Scanner sc = new Scanner(System.in)){

        System.out.print("Enter the number of rows : ");
        int rows = sc.nextInt();
        // System.out.print("Enter the number of columns : ");
        // int columns = sc.nextInt();

        for(int i = 1 ; i <= rows; i++){
        for(int j = 1 ; j <= i; j++){

            System.out.print(j);

            }
            System.out.println();
        }
    }
}
}