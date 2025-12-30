import java.util.*;
public class conditional_statements {
    
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        /* AGE VERIFIER */

        // int age = sc.nextInt();

        // if (age > 18) {
        //     System.out.println("Adult");}
        // else {
        //     System.out.println("Not an Adult");
        // }
        /* ODD EVEN  */

        // int num = sc.nextInt();

        // if (num%2==0){
        //     System.out.println("Even");
        // }
        // else {
        //     System.out.println("Odd");
        // }

        /* GREATER OR LESSER */

        // int a = sc.nextInt();
        // int b = sc.nextInt();

        // if (a > b) {System.out.println("A is greater"); }
        // else if ( b > a){  System.out.println("B is greater"); }   
        // else {System.out.println("Both A & B are equal to each other"); }
        
        /* PRACTICALL THE SAME AS ABOVE BUT USING SWITCH CASES */
        int input = sc.nextInt();
        switch(input){
            case 1 : System.out.println("Konnichiwa");
            break ;
            case 2 : System.out.println("Hello");
            break;
            case 3 : System.out.println("Namaste");
            break;
            default : System.out.println("Kya karna chahte ho ??");
        }
    
    }
            }



