<?php 
//Creating a function to resolve the sum 
function solveMeFirst($a,$b){
    return $a + $b;
}

//Creating variables and showing the result to user
$num1 = (int)readline();
$num2 = (int)readline();
echo solveMeFirst($num1,$num2);

?>