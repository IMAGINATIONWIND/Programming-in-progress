package patterns.Advanced_patterns;

import java.util.*;

public class Butterfly {
    public static void main(String[] args){
        try(Scanner sc = new Scanner(System.in)){

        System.out.print("Kindly enter the number of rows : ");
        int rows = sc.nextInt();
        for (int i = 1 ; i <= rows; i++){

            for (int j = 1 ; j <= i ; j++){
                System.out.print("*");
            }

            for (int k = 1 ; k <= (rows-(i))*2 ; k++){
                System.out.print(" ");
            }

            for (int t = 1 ; t <= i ; t++){
                System.out.print("*");
            }

            System.out.println();

        }
        for (int i = rows ; i >= 1; i--){

            for (int j = 1 ; j <= i ; j++){
                System.out.print("*");
            }

            for (int k = 1 ; k <= (rows-(i))*2 ; k++){
                System.out.print(" ");
            }

            for (int t = 1 ; t <= i ; t++){
                System.out.print("*");
            }

            System.out.println();

        }
    }
}
}