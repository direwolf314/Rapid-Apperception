<?php

$_POST['file'] = urldecode($_POST['file']);

//echo "php " . $_POST['file'];
$file = fopen("/" . $_POST['file'], "r") or die("Unable to open file!");

while(!feof($file)) {
  echo "<p>" . fgets($file) . "</p>";
}

fclose($file);

?>
