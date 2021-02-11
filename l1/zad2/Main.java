import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int time=0, n=0;
        int[][] distances=null;

        try{
            String line=scan.nextLine();
            String[] numbers=line.trim().split("\\s+");
            time=Integer.parseInt(numbers[0]); 
            n= Integer.parseInt(numbers[1]);   
            distances= new int[n][n];

            for(int i=0; i<n; i++){
                line=scan.nextLine();
                numbers=line.trim().split("\\s+");

                for(int j=0; j<numbers.length; j++)
                        distances[i][j]=Integer.parseInt(numbers[j]);                     
            }
            scan.close();
        }catch (NumberFormatException nfe){
            System.out.println("Na wejsciu prosze podac tylko liczby typu int \noddzielone spacjami");
            System.exit(0);
        }

        TabuSearch Searcher= new TabuSearch(new TSP(distances, n));
        Searcher.findBestSolution(time, n);
        System.out.println(Searcher.getBestValue());
        int[] solution= Searcher.getBestSolution();
        for(int i=0; i<solution.length; i++)
            System.err.print(solution[i]+" ");

        System.err.println();

    }
}