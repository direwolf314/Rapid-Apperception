<?php
//echo "File is: " . $_POST['file'];
//if( isset($_POST['tag_name']) ) {
    //echo "tag_name is: " . $_POST['tag_name'];
//}

$_POST['file'] = urldecode($_POST['file']);
if( isset($_POST['tag_name']) ) {
    $_POST['tag_name'] = urldecode($_POST['tag_name']);
    echo "Listing matches for tag_name: " . $_POST['tag_name'] . '.';
} else {
    echo "Listing matches for all tags.";
}

$base_dir = "/";

$m = new MongoClient();
$db = $m->RapidApperception;
$col = $db->TaggingInfo;

$query = array();
if( !isset($_POST['tag_name']) ) {
    $query = array( 'file_path' => $_POST['file'] );
} else {
    $query = array( 'file_path' => $_POST['file'] ,
                    'tag_name' => $_POST['tag_name']);
}

$cursor = $col->find( $query );
$line_nums = "";
foreach ( $cursor as $document ){
  $line_nums = $line_nums . $document["line_num"] . ",";
}
//echo "Line_nums:" . $line_nums;

$file = fopen($base_dir . $_POST['file'], "r") or die("Unable to open file!");

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
