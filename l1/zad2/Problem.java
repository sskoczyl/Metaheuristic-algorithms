public interface Problem{
    public int[] startSolution();
    public int solutionEvaluation(int[] dist);
    public int[][] generateNeighbor(int n, int perms);
}