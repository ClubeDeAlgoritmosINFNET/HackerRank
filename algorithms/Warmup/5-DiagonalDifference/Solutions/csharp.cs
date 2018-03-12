using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static int diagonalDifference(int[][] a) {
            int x = 0;
            int dig1 = 0;
            int dig2 = 0;
            foreach(int[] row in a)
            {
                dig1 += a[x][x];
                x += 1;
            }

            x = 0;
            int y = 1;
            foreach (int[] row in a)
            {
                
                dig2 += a[x][a.Length - y];

                x += 1;
                y += 1;
            }

            return Math.Abs(dig1 - dig2);
    }

    static void Main(String[] args) {
        int n = Convert.ToInt32(Console.ReadLine());
        int[][] a = new int[n][];
        for(int a_i = 0; a_i < n; a_i++){
           string[] a_temp = Console.ReadLine().Split(' ');
           a[a_i] = Array.ConvertAll(a_temp,Int32.Parse);
        }
        int result = diagonalDifference(a);
        Console.WriteLine(result);
    }
}
