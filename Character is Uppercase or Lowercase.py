import java.util.Scanner;
public class Alphabets{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        char chr=sc.next().charAt(0);
       if(chr>='A' && chr<='Z'){
        System.out.println("uppercase alphabet");
       }
       else if(chr>='a' && chr<='z'){
        System.out.println("lowercase alphabet");
       }
       else{
        System.out.println("not an alphabet");
       }
    }
}