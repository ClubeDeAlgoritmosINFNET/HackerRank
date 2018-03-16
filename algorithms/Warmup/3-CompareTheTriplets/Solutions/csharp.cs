using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static int[] solve(int a0, int a1, int a2, int b0, int b1, int b2){
            int[] alice = new int[] { a0, a1, a2 };
            int[] bob = new int[] { b0, b1, b2 };
            int aliceScore = 0;
            int bobScore = 0;
            int[] result = new int[2];

            for(int i = 0; i < 3; i++)
            {
                if(alice[i] > bob[i])
                {
                    aliceScore += 1;
                }
                if (alice[i] < bob[i])
                {
                    bobScore += 1;
                }
            }
            result[0] = aliceScore;
            result[1] = bobScore;

            return result;
            
    }

    static void Main(String[] args) {
        string[] tokens_a0 = Console.ReadLine().Split(' ');
        int a0 = Convert.ToInt32(tokens_a0[0]);
        int a1 = Convert.ToInt32(tokens_a0[1]);
        int a2 = Convert.ToInt32(tokens_a0[2]);
        string[] tokens_b0 = Console.ReadLine().Split(' ');
        int b0 = Convert.ToInt32(tokens_b0[0]);
        int b1 = Convert.ToInt32(tokens_b0[1]);
        int b2 = Convert.ToInt32(tokens_b0[2]);
        int[] result = solve(a0, a1, a2, b0, b1, b2);
        Console.WriteLine(String.Join(" ", result));
        

    }
}