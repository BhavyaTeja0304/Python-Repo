import java.util.Scanner;
public class Number{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        for(int i=a;i>0;i--){
            System.out.printf("%d ",i);
        }
    }
}