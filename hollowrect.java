package patterns;

import java.util.*;
public class hollowrect {
    public static void main(String[] args){
       try( Scanner sc = new Scanner(System.in)){
        
        System.out.print("Enter the rows: ");
        int rows = sc.nextInt();
        System.out.print("Enter the columns: ");
        int columns = sc.nextInt();


        for (int i = 1; i <=rows ; i++ ){
        for (int j = 1; j <=columns ; j++ ){
            if(i==1||j==1||i==rows||j==columns){
                System.out.print("*");}
            else {
                System.out.print(" ");
            }
            }
            System.out.println();
            }
        }    
}
}