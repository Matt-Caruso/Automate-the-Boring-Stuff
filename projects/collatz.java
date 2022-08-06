package projects;
import java.util.Scanner;
public class collatz{
    public static int num;
    public static int v = 0;
    public static int x = 0;
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    System.out.println("Enter A Number: ");
    num = input.nextInt();
    x = num;
    while(v != 1){     
    coll();
    }
    }
    public static void coll(){
        if(x % 2 == 0)
            x = (x / 2);
        else
            x = (num * x + 1);
        v = x;
        System.out.println(x);

    }
}


