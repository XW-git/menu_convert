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
  line-height: 28pt
 
}
.menu_css tt_ds {         
  display: block;
  text-transform: none;
  font-size: 15px;
  padding: 0 20px 10px;
  line-height: 12px;
  font-style: normal;
  color: white;
  font-family:corbel;
  text-align: center;
   line-height: 0pt 
  
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

$file_name =  ABSPATH.'restaurant_menu/b.txt';

$lines = file($file_name);

foreach ($lines as $line_num => $line) {

echo $line;
}

?>
</div>
</body>