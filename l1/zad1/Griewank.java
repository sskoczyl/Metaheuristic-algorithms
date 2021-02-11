import java.lang.Math;

public class Griewank implements AbstractFunction{
    @Override
    public double getValueAtX(double[] vector){
        double sum = 0;
        double product = 1;
        for(int i =0; i < vector.length; i++){
            sum += Math.pow(vector[i], 2);
            product *= Math.cos(vector[i]/Math.sqrt(i+1));
        }

        return 1 + sum/4000 - product;
    }
}