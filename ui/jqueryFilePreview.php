<?php
$m = new MongoClient();
$db = $m->RapidApperception;
$col = $db->TaggingInfo;

$query = array( 'file_path' => $_POST['file'] );
$cursor = $col->find( $query );

foreach ($cursor as $document) {
    echo $document["key_match"] . "\n";
}

$_POST['file'] = urldecode($_POST['file']);

//echo "php " . $_POST['file'];
$file = fopen("/" . $_POST['file'], "r") or die("Unable to open file!");

while(!feof($file)) {
  echo "<p>" . fgets($file) . "</p>";
}

fclose($file);

?>
