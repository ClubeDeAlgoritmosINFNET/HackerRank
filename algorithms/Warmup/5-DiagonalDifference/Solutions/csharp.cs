using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static int diagonalDifference(int[][] a) {
        var lastPosition = a.Length - 1;
        int diagonalOne = 0;
        int diagonalTwo = 0;
        
        for(int position = lastPosition; position >= 0; position--){
            diagonalOne += a[position][position];
            diagonalTwo += a[position][lastPosition - position];
        }
        
        return Math.Abs(diagonalOne - diagonalTwo);
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
