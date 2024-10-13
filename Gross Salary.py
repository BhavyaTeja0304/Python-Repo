import java.util.Scanner;
public class GrossSalary{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        float bs=sc.nextFloat();
        float g=0;
        float d=0;
        float h=0;
        if(bs<=10000){
            h=0.2f*bs;
            d=0.8f*bs;
        }
        else if(bs<=20000){
            h=0.25f*bs;
            d=0.9f*bs;
        }
        else{
            h=0.3f*bs;
            d=0.95f*bs;
        }
        g=bs+h+d;
        System.out.printf("%.2f",g);

    }
}