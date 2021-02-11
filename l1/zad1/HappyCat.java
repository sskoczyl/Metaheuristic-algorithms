import java.lang.Math; 

public class HappyCat implements AbstractFunction{
    @Override
    public double getValueAtX(double[] vector){     //returns h(vector)
        double sum=0, norm=0;

        for(int i=0; i<vector.length; i++){
            norm+=Math.pow(vector[i], 2.0);
            sum+=vector[i];
        }

        double value=Math.pow(norm-4.0, 2);
        value=Math.pow(value, 1/8.0);
        value+=0.25*(0.5*norm+sum)+0.5;
        
        return value;
    }

}