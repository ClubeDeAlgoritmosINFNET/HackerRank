using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    static int alice = 0;
    static int bob = 0;
        
    static int[] solve(int a0, int a1, int a2, int b0, int b1, int b2){
        var zero = Compare(a0, b0);
        var one = Compare(a1, b1);
        var two = Compare(a2, b2);
        
        Validate(zero);
        Validate(one);
        Validate(two);
        return new int[2]{alice, bob};
    }
    
    static void Validate(int val){
        if(val == 1){
            alice += 1;
        }else if(val == -1){
            bob += 1;
        }
    }
    
    static int Compare(int a, int b){
        if(a > b){
            return 1;
        }else if(b > a){
            return -1;
        }else{
            return 0;
        }
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
