public class TabuSearch{

    private final Agent Problem;
    private int[] bestSolution;

    public TabuSearch(Agent prblm){
        this.Problem=prblm;
    }

    public int[] getBestSolution(){
        return bestSolution;
    }

    public int getBestValue(){
        return Problem.solutionEvaluation(bestSolution);
    }

    public void findBestSolution(int seconds){
        bestSolution=Problem.startSolution();
        int bestLength=Problem.solutionEvaluation(bestSolution);
        int[][] Tabu=generateTabu(bestLength);
        int[] perms= new int[2];
        long t= System.currentTimeMillis();
        long end = t+seconds*1000;

        while(System.currentTimeMillis() < end){  
              perms=Problem.generateNeighbor(bestSolution);
            
              if(Tabu[perms[0]][perms[1]]==0){
                  swapValues(bestSolution, perms[1], perms[0]);
                  int newLenght = Problem.solutionEvaluation(bestSolution);
  
                  if(newLenght > 0){
                          bestLength = newLenght;
                          int[] temp = new int[bestLength];
                          System.arraycopy(bestSolution, 0, temp, 0, bestLength);
                          bestSolution = temp;
                  }else{
                      tabuCare(Tabu, perms[1], perms[0]);
                      swapValues(bestSolution, perms[1], perms[0]);
                  }
              }
           
        }
    }

    private int[][] generateTabu(int n){
        int tab[][]=new int[n][n];

        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                tab[i][j]=0;

        return tab;
    }

    private void swapValues(int[] arr, int x, int y){
        int help= arr[x];
        arr[x]=arr[y];
        arr[y]=help;
    }

    private void tabuCare(int[][] tabu, int x, int y){
        for(int i=0; i<tabu.length; i++)
            for(int j=0; j<tabu.length; j++)
                if(tabu[i][j]>0)
                    tabu[i][j]--;
        
        tabu[x][y]=tabu.length;
    }

}