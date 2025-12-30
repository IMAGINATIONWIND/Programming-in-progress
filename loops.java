import java.util.*;
public class loops {
    public static void main(String[] args){
        for (int i = 0; i < 5 ; i++){
            System.out.print("NUMBER "+i+" ");
        }
        // int i = 0
        // System.out.println();
        // while(i < 11){
        //     System.out.print("jonas "+i+"  ");
        //     ++i;
        // }
        
        System.out.println();

        int i = 0 ;
        do {
            System.out.print("mary "+i+" ");
            i++;
        } while(i < 11);

        System.out.println();

        int j = 15 ;
        do {
            System.out.print("mary jane "+j+" ");
            j++;
        } while(j < 11);//Don't you ever forget teh ; after while in do while
    }
}
