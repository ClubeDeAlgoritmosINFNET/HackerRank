<?php 
    //function to sum all array elements
    function simpleArraySum($n,$arr){
        return array_sum($arr);
    }
    
    $n = readline(); //getting the size of the array;
    $arr = readline(); //getting the elements to sum;
    $arr = array_map('trim', explode(' ', $arr)); //removing whitespaces and turn the elements in an array
    echo simpleArraySum($n, $arr); //showing the sum of the array, calling the function simpleArraySum() and passing the parametres
    
?>
