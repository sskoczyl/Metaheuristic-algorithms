import java.util.*;

public class TabuSearch{

    private final Problem Problem;
    private int[] bestSolution;

    public TabuSearch(Problem prblm){
        this.Problem=prblm;
    }

    public int[] getBestSolution(){
        return bestSolution;
    }

    public int getBestValue(){
        return Problem.solutionEvaluation(bestSolution);
    }

    public void findBestSolution(int seconds, int n){
        int cnt=25;
        int[][] tabu=generateTabu(n);
        int[][] perms= Problem.generateNeighbor(n, cnt);
        bestSolution=Problem.startSolution(); 
        int bestValue=Problem.solutionEvaluation(bestSolution);
        long t= System.currentTimeMillis();
        long end = t+seconds*1000;

        while(System.currentTimeMillis() < end){    
            for(int i=0; i<cnt; i++){
                int newSolution[]=bestSolution.clone();
                newSolution=swapValues(newSolution, perms[i][0], perms[i][1]).clone();
                perms[i][2]=Problem.solutionEvaluation(newSolution);
            }

            sortPerms(perms, 2);

            for(int i=0; i<cnt; i++)
                if(tabu[perms[i][0]][perms[i][1]]==0 || bestValue>perms[i][2]){
                    bestSolution=swapValues(bestSolution, perms[i][0], perms[i][1]).clone();
                    tabu[perms[i][0]][perms[i][1]]=25;

                    if(bestValue>perms[i][2])
                        bestValue=perms[i][2];
                        
                    break;
                }

            reducePenalty(tabu);
            perms=Problem.generateNeighbor(n, cnt);
        }
    }

    private int[][] generateTabu(int n){
        int tab[][]=new int[n][n];

        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                tab[i][j]=0;

        return tab;
    }

    private int[] swapValues(int[] arr, int x, int y){
        int help= arr[x];

        arr[x]=arr[y];
        arr[y]=help;

        return arr;
    }

    private static void sortPerms(int arr[][], int col){

         Arrays.sort(arr, new Comparator<int[]>() { 
            @Override 
            public int compare(final int[] entry1, final int[] entry2) { 
              if (entry1[col] > entry2[col]) 
                  return 1; 
              else
                  return -1; 
            } 
          });  
    }

    private int[][] reducePenalty(int[][] tabu){
        for(int i=0; i<tabu.length; i++)
            for(int j=0; j<tabu.length; j++)
                if(tabu[i][j]>0)
                    tabu[i][j]--;

        return tabu;
    }

}
