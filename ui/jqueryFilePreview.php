<?php
$_POST['file'] = urldecode($_POST['file']);

$m = new MongoClient();
$db = $m->RapidApperception;
$col = $db->TaggingInfo;

$query = array( 'file_path' => $_POST['file'] );
$cursor = $col->find( $query );
$line_nums = "";
foreach ( $cursor as $document ){
  $line_nums = $line_nums . $document["line_num"] . ",";
}

$file = fopen("/" . $_POST['file'], "r") or die("Unable to open file!");

//WARN
//right now, language name for prism attribute is completely based on extension
// of file. Probably not sufficient in all cases
$ext = pathinfo($_POST['file'], PATHINFO_EXTENSION);
echo "<pre data-line=\"" . $line_nums . "\"><code class=\"language-" . $ext . "\">";

while(!feof($file)) {
  echo htmlspecialchars(fgets($file));
}
echo "</code></pre>";

fclose($file);

?>
