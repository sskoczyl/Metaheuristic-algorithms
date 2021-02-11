import java.util.Random;
import java.util.*;

public class Agent{

    private final int[][] grid;
    private final int[] coords;
    private final int[][] moves = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

    public Agent(int[][] map){
        this.grid=map;
        coords=findAgent();
    }

    public int[] startSolution(){
        ArrayList<Integer> path = new ArrayList<Integer>();
        int moved;
        int idx = 0, end = 0, length = 0;
        int[] move;
        int[] newCoords = coords.clone();
        
        while(grid[newCoords[0]][newCoords[1]] != 8){
            do{
                move = moves[idx].clone();
                newCoords[0]+=move[0];
                newCoords[1]+=move[1];
                length++;    
                path.add(idx);

                if(exitSurrounding(end, newCoords)){
                    move = moves[end];
                    newCoords[0]+=move[0];
                    newCoords[1]+=move[1];
                    length++;    
                    path.add(end);
                }               
            } while(grid[newCoords[0]][newCoords[1]] != 1 && grid[newCoords[0]][newCoords[1]] != 8);

            if(grid[newCoords[0]][newCoords[1]]==1){
                newCoords[0]-=move[0];
                newCoords[1]-=move[1];
                length--;
                path.remove(path.size()-1);
                
                if(idx==0){
                    idx=2;
                    end=0;
                    moved=0;
                }else{
                    moved=Integer.valueOf(idx);
                    idx=makeTurn(end);
                    end=moved; 
                }
            }
        }

        int[] tab = new int[length];
        for(int i = 0; i<length; i++){
            tab[i] = path.get(i);
        }      
        return tab;
    }

    public int solutionEvaluation(int[] newRoute){
        int idx, value=0;
        int[] mv, newCoords= coords.clone();
        
        for(int i=0; i< newRoute.length; i++){
            value++;
            idx=newRoute[i];
            mv=moves[idx];
            newCoords[0]+=mv[0];
            newCoords[1]+=mv[1];

            if(newCoords[0]>=grid.length || newCoords[0]<0)
                return -1;
            if(newCoords[1]>=grid[0].length || newCoords[1]<0)
                return -1;
            if(grid[newCoords[0]][newCoords[1]] == 8)
                return value;
        }

        return -1;
    }

    private boolean exitSurrounding(int direction, int[] newCoords){
        int[] mv = moves[direction];

        try{
            if(grid[newCoords[0] + mv[0]][newCoords[1]+mv[1]] == 8) 
                return true; 
                
        }catch(Exception ex){ return false;}
        
        return false; 
    }

	public int[] generateNeighbor(int[] arr) {
        Random r = new Random();
        int i =0, j=0;

        while(i == j && arr[i] == arr[j]){
            i = r.nextInt(arr.length);
            j = r.nextInt(arr.length);
        }

        if( i < j){
            int[] perm = {i, j};
            return perm;
        }else{
            int[] perm = {j, i};
            return perm;
        }

    }
    
    private int[] findAgent(){
        int arr[]= new int[2];

        for(int i=0; i<grid.length; i++)
            for(int j=0; j<grid[i].length; j++)
                if(grid[i][j]==5){
                    arr[0]=i;
                    arr[1]=j;
                    break;
                }    
        
        return arr;
    }   

    private int makeTurn(int direction){
        if(direction==0)
            return 1;
        else if(direction==1)
            return 0;
        else if(direction==2)
            return 3;
        else if(direction==3)
            return 2;
        else    
            return -1;
    }
}