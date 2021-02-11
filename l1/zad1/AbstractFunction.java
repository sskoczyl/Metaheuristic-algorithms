import java.util.Random;

public interface AbstractFunction{

    public  double getValueAtX(double[] vector);

    default double[] randomArgument(int dimensions){   //returns random n-dimensional vector
        Random r = new Random();
        double[] tab= new double[dimensions];

        for(int i=0; i<tab.length; i++)
            tab[i]=r.nextDouble()+(double)r.nextInt(100)-50;

        return tab;
    }

    default double[] randomNeighbor(double[] base,double radius){
        Random r = new Random();
        double[] newVector=new double[base.length];
        double norm=0;
        
        for(int i = 0; i< base.length; i++){
            newVector[i] = r.nextGaussian();
            norm += Math.pow(newVector[i] - base[i], 2);        
        }
        norm = Math.sqrt(norm);
       
       
        for(int i =0; i < base.length; i++){
            newVector[i] *= radius;
            newVector[i] /= norm;              
        }   

        return newVector;
    }
}