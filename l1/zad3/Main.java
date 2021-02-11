import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int time=0, n=0, m=0;
        int[][] grid=null;

        try{
            String line=scan.nextLine();
            String[] numbers=line.trim().split("\\s+");

            time=Integer.parseInt(numbers[0]); 
            n= Integer.parseInt(numbers[1]);   
            m= Integer.parseInt(numbers[2]);

            grid= new int[n][m];

            for(int i=0; i<n; i++){
                line=scan.nextLine();
                char[] gridFields=line.toCharArray();

                for(int j=0; j<m; j++)
                    grid[i][j]=Character.getNumericValue(gridFields[j]);                     
            }

            scan.close();
        }catch (NumberFormatException nfe){
            System.out.println("Bledne dane wejsciowe");
            System.exit(0);
        }

        Agent Agent=new Agent(grid);
        TabuSearch Searcher= new TabuSearch(Agent);
        Searcher.findBestSolution(time);

        int length=Searcher.getBestValue();
        System.out.println(length);

        int[] solution= Searcher.getBestSolution();

        for(int i=0; i<length; i++)
            if(solution[i]==0)
                System.err.print("U");
            else if(solution[i]==1)
                System.err.print("D");
            else if(solution[i]==2)
                System.err.print("R");
            else if(solution[i]==3)
                System.err.print("L");

        System.err.println();
    }
}