<!-- read a txt file and parse menu to html -->
<head>
<title>Page Title</title>
<style>

.menu_css {    

  font-size: 22px;
  color: #df4623;
  background-color: #112029;

}

.menu_css tt {         
  display: block;
  text-transform: none;
  font-size: 28px;
   font-weight: bold;
  margin: 10px;
  color:  #df4623;
  text-align: center;
  font-family:sail;
  
}

.menu_css ds {         
  display: block;
  text-transform: none;
  font-size: 15px;
  padding: 0 5px 15px;
  line-height: 12px;
  font-style: normal;
  color: white;
  font-family:corbel;
  
}

.menu_css pr {       
  float: right;
  font-style: normal;
}
</style>
</head>

<body>
<div class="menu_css">

<?php

$test_csv =  ABSPATH.'restaurant_menu/a.txt';

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
                echo  "<pr>". $price ."</pr>". "<br>";
            }            
            break;
       case 2:
            echo "<ds>". $line. "</ds>";
            break;
       default:
            break; 
    } 
}

?>
</div>
</body>