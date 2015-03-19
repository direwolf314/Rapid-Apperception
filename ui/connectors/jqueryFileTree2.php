<?php
//
// jQuery File Tree PHP Connector
//
// Version 1.01
//
// Cory S.N. LaViska
// A Beautiful Site (http://abeautifulsite.net/)
// 24 March 2008
//
// History:
//
// 1.01 - updated to work with foreign characters in directory/file names (12 April 2008)
// 1.00 - released (24 March 2008)
//
// Output a list of files for jQuery File Tree
//

$_POST['dir'] = urldecode($_POST['dir']);
if (isset($_POST['tag_name'])) {
    $_POST['tag_name'] = urldecode($_POST['tag_name']);
}

$base_dir = "/";

$m = new MongoClient();
$db = $m->RapidApperception;
$col = $db->TaggingInfo;

if( file_exists($base_dir . $_POST['dir']) ) {
    $files = scandir($base_dir . $_POST['dir']);
    natcasesort($files);
    if( count($files) > 2 ) { /* The 2 accounts for . and .. */
		echo "<ul class=\"jqueryFileTree\" style=\"display: none;\">";

        foreach( $files as $file ) {
            if( file_exists($base_dir . $_POST['dir'] . $file) && 
                $file != '.' && $file != '..') 
            {

                $path = htmlentities($_POST['dir'] . $file);
                $name = htmlentities($file);

                if (is_dir($base_dir . $_POST['dir'] . $file) ) {
                    // All dirs
                    $query = array();
                    if( !isset($_POST['tag_name']) || $_POST['tag_name'] == '') {
                        // Match all tags in all files in this dir
                        $query = array( 'file_path' => array('$regex' => $path . '/*'));
                    } else {
                        // Match the given tag in all files in this dir
                        $query = array( 'file_path' => array('$regex' => $path . '/*'),
                                        'tag_name' => $_POST['tag_name']);
                    }                   
                    $count = $col->count($query);
                    $name = $name . '  - ' . $count . ' matches';

                    echo "<li class=\"directory collapsed\">
                          <a href=\"#\" rel=\"" . $path .
                          "/\">" . $name . "</a></li>";

                } else {
                    // All files
                    $query = array();
                    if( !isset($_POST['tag_name']) || $_POST['tag_name'] == '') {
                        // Count all tags in this file
                        $query = array( 'file_path' => array('$regex' => $path));
                    } else {
                        // Count number of occurences of the given tag in this file
                        $query = array( 'file_path' => array('$regex' => $path),
                                        'tag_name' => $_POST['tag_name']);
                    }                   
                    $count = $col->count($query);
                    $name = $name . '  - ' . $count . ' matches';

                    $ext = preg_replace('/^.*\./', '', $file);
                    echo "<li class=\"file ext_$ext\">
                          <a href=\"#\" rel=\"" . $path . 
                          "\">" . $name . "</a></li>";
                }
            }
		}
		echo "</ul>";	
	}
} else {
    echo 'File didnt exist';
}

?>
