public class LocalSearch{

    private final AbstractFunction Function;
    private final double radius;
    private double[] minCoords;

    public LocalSearch(AbstractFunction function, double radius){
        this.radius=radius;
        this.Function=function;
    }

    public double[] findMinima(int seconds, int dimensions){      //returns n-dimensional vector and in n+1 field value of f(vector) 
        minCoords=Function.randomArgument(dimensions);
        double minVal=Function.getValueAtX(minCoords);
        long t= System.currentTimeMillis();
        long end = t+seconds*1000;

        while(System.currentTimeMillis() < end){            

            double[] randCoords=Function.randomNeighbor(minCoords, radius);
            double newValue=Function.getValueAtX(randCoords);

            if(newValue< minVal){
                minCoords=randCoords;
                minVal=newValue;
            }
    
        }

        double[] outcomeArr= new double[dimensions+1];

        for(int i=0; i<dimensions; i++)
            outcomeArr[i]=minCoords[i];

        outcomeArr[dimensions]=minVal;

        return outcomeArr;
    }

}