import java.util.Scanner;

public class Main{
    public static void main(String[] args){         //Driver function
        Scanner scan = new Scanner(System.in);
        LocalSearch Searcher;
        double radius=1.0;
        int time=2;
        int dimensions=4;
        int function=0;

        try{

            String line=scan.nextLine();
            String[] numbers=line.trim().split("\\s+");

            time=Integer.parseInt(numbers[0]); 
            function= Integer.parseInt(numbers[1]);   

        }catch (NumberFormatException nfe){
            System.out.println("Na wejsciu prosze podac dwie liczby typu int");
            System.exit(0);
        }

        if(function==0)
            Searcher=new LocalSearch(new HappyCat(), radius);
        else
            Searcher=new LocalSearch(new Griewank(), radius);
        
        double outcome[]=Searcher.findMinima(time, dimensions);
        
        for(int i=0; i< outcome.length; i++)
            System.out.print(outcome[i]+" ");

        System.out.println();
    }
}