<!-- read a txt file and parse menu to html -->
<head>
<title>Page Title</title>
<style>

.rm-content {

  font-size: 25px;
  color: #df4623;
  background-color: #112029;

}
.rm-content tt {
  display: block;
  text-transform: none;
  font-size: 30px;
  margin: 10px;
  color:  #df4623;
  text-align: center;
  
}

.rm-content i {
  display: block;
  text-transform: none;
  font-size: 15px;
  padding: 0 5px 15px;
  line-height: 12px;
  font-style: normal;
  color: white;
  
}

.rm-content em {
  float: right;
  font-style: normal;
}
</style>
</head>

<body>
<div class="rm-content">

<?php

$test_csv =  ABSPATH.'restaurant_menu/Chef’s Special Rolls.txt';

$i = 0;
$lines = file($test_csv);

foreach ($lines as $line_num => $line) {
$str=$line;
    if (bin2hex($line)=="0d0a"){
    // new item starts
    $i = 0;
    }
    else{
    $i = $i+1;
    }
      
    switch ($i) {
        case 0:
            break;
        case 1: 
            $price=strrchr($line,"\t"); 
            if($price==""){
                echo "<tt>". $line. "</tt>";
            }
            else{ 
                $dish_name=str_replace($price,"",$line);
                echo  $dish_name;
                echo  "<em>". $price ."</em>". "<br>";
            }            
            break;
       case 2:
            echo "<i>". $line. "</i>";
            break;
       default:
            break; 
    } 
}

?>
</div>
</body>