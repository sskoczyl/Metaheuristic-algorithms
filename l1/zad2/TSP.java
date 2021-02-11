import java.util.HashSet;
import java.util.Random;

public class TSP implements Problem{

    private final int[][] distances;
    private final int cities;

    public TSP(int[][] dist, int n){
        this.distances=dist;
        this.cities=n;
    }

    @Override
    public int[] startSolution(){
        int[] solution=new int[cities+1];
        solution[0]=1;
        solution[cities]=1;
        HashSet<Integer> used = new HashSet<Integer>();

        for (int i = 1; i < cities; i++) {
            int add = (int)(Math.random() * (cities-1))+ 2; 
            
            while (used.contains(add)) 
                add = (int) (Math.random() * (cities-1)) +2; 
  
            used.add(add);
            solution[i] = add;
        }   
        return solution;
    }

    @Override
    public int solutionEvaluation(int[] newRoute){
        int value=0;

        for(int i=1; i<newRoute.length; i++){
            value+=distances[newRoute[i-1]-1][newRoute[i]-1];
        }
        
        return value;
    }

	@Override
	public int[][] generateNeighbor(int n, int cnt) {
        Random r = new Random();
        int[][] perms=new int[cnt][3];
        HashSet<int[]> used = new HashSet<int[]>();

        for(int i=0; i<cnt; i++){
            for(int j=0; j<2; j++){

                int[] x=new int[2];

                do{
                    do{
                        perms[i][j]=r.nextInt(n-1)+1;  
                    }while(j==1 && perms[i][0]==perms[i][1]);

                    if(perms[i][0]<perms[i][1]){
                        int help=perms[i][1];
                        perms[i][1]=perms[i][0];
                        perms[i][0]=help;
                    }

                    x[0]=perms[i][0];
                    x[1]=perms[i][1];

                }while(used.contains(x));   

                used.add(x);
            }
        }
		return perms;
	}
}