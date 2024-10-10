import java.util.Scanner;
public class Colour{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String letter=sc.nextLine();
        if(letter=="V"){
            System.out.println("Violet");
        }
        else if(letter.equals("I")){
            System.out.println("Indigo");
        }
        else if(letter.equals("B")){
            System.out.println("Blue");
        }
        else if(letter.equals("G")){
            System.out.println("Green");
        }
        else if(letter.equals("Y")){
            System.out.println("Yellow");
        }
        else if(letter.equals("O")){
            System.out.println("Orange");
        }
        else if(letter.equals("R")){
            System.out.println("Red");
        }
        else{
            System.out.println(-1);
        }
    }
}